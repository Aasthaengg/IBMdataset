N = int(input())
B = list(map(int,input().split()))

ans = []
for i in range(N-1,-1,-1):
    for j in range(i,-1,-1):
        if B[j] == j+1:
            ans.append(B[j])
            del B[j]
            break

if len(ans) == N:
    print('\n'.join(map(str,ans[::-1])))
else:
    print(-1)