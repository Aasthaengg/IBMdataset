N = int(input())

A = list(map(int,input().split()))
s = 0
for i,a in enumerate(A):
    if i%2:
        s -= a
    else:
        s += a

ans = [-1 for i in range(N)]
ans[0] = s

for i in range(1,N):
    ans[i] = (A[i-1]-ans[i-1]//2)*2
print(*ans)
