n = int(input())
A = list(map(int,input().split()))
L = {}
R = {}
ans = 0
for i,j in enumerate(A):
    if i+j in L:
        L[i+j] += 1
    else:
        L[i+j] = 1
    if i-j in R:
        R[i-j] += 1
    else:
        R[i-j] = 1
for i,j in L.items():
    if i in R:
        ans += j*R[i]
print(ans)