N = int(input())
A = list(map(int,input().split()))
res = [0]* N

for i in range(N-1):
    res[i+1] = A[i+1] - res[i]
res[0]  = (A[0] - res[0] - res[-1])//2
for i in range(N-1):
    res[i+1] = A[i+1] - res[i]
ans = [2*res[i-1] for i in range(N)]
print(*ans)