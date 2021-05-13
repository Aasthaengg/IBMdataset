A = input().strip()
N = len(A)
tot = 1+(N*(N-1))//2
C = {chr(i):[] for i in range(97,123)}
for i in range(N):
    C[A[i]].append(i)
cnt = 0
for a in C:
    n = len(C[a])
    cnt += (n*(n-1))//2
print(tot-cnt)