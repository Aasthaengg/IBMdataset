N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if sum(A) < sum(B):
    print(-1)
    exit(0)

C = [A[k]-B[k] for k in range(N)]
C.sort()
t = 0
ans = 0
for k in range(N):
    if C[k] >= 0:
        break
    else:
        t -= C[k]
        ans += 1

for k in range(N-1,-1,-1):
    if t <= 0:
        break
    else:
        t -= C[k]
        ans += 1

print(ans)
