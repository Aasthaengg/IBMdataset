N = int(input())
A = list(map(int,input().split()))

ans = []
res = 0
for i in range(N):
    if i%2==0:
        res += A[i]
    else:
        res -= A[i]

ans.append(res)

for i in range(1,N):
    res = 2*A[i-1]-ans[-1]
    ans.append(res)

print(*ans)