#52d
N,A,B = map(int, input().split())
X_list = [int(e) for e in input().split()]

diff_X_list = [X_list[i]-X_list[i-1] for i in range(1,N)]

ans = 0
for diff_X in diff_X_list:
    if diff_X * A >= B:
        ans += B
    else:
        ans += diff_X * A
        
print(ans)