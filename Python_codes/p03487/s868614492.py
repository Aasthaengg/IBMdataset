N = int(input())
A = list(map(int,input().split()))
C = {}
for i in range(N):
    a = A[i]
    if a not in C:
        C[a] = 0
    C[a] += 1
cnt = 0
for a in C:
    if C[a]<a:
        cnt += C[a]
    else:
        cnt += C[a]-a
print(cnt)