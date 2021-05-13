N = int(input())
A = list(map(int,input().split()))
C = {}
cnt = 0
for i in range(N):
    a = A[i]
    if a>N:
        cnt += 1
    else:
        if a not in C:
            C[a]=0
        C[a] += 1
for a in C:
    if a>C[a]:
        cnt += C[a]
    elif a<C[a]:
        cnt += C[a]-a
print(cnt)