N,*A=map(int,open(0).read().split())
M = max(A); m = min(A)
ans = []
if -m < M:
    idx = A.index(M)
    for i in range(N):
        A[i] += A[idx]
        ans.append((idx, i))
    for i in range(1, N):
        A[i] += A[i-1]
        ans.append((i-1, i))
else:
    idx = A.index(m)
    for i in range(N):
        A[i] += A[idx]
        ans.append((idx, i))
    for i in range(N-1, 0, -1):
        A[i-1] += A[i]
        ans.append((i, i-1))
#print(*A)
print(len(ans))
for x, y in ans:
    print(x+1, y+1)
