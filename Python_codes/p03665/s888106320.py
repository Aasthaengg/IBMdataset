N,P = map(int,input().split())
A = list(map(int,input().split()))
ans = [1,0]
for a in A:
    if a%2:
        ans[1],ans[0] = ans[1] + ans[0], ans[1] + ans[0]
    else:
        ans[0] = ans[0]*2
        ans[1] = ans[1]*2
print(ans[P])