N = int(input())
A = list(map(int,input().split()))
C = {}
for i in range(N):
    a = A[i]
    if a not in C:
        C[a] = 0
    C[a] += 1
if len(C)==N:
    print("YES")
else:
    print("NO")