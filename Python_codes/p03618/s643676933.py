A = input().strip()
C = {chr(i):0 for i in range(97,123)}
n = len(A)
for i in range(n):
    C[A[i]] += 1
cnt = 0
for a in C:
    cnt += (C[a]*(C[a]-1))//2
print(1+(n*(n-1))//2-cnt)