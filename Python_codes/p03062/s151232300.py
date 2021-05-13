N = int(input())
A = list(map(int,input().split()))
m = 0
z = 0
for i in range(N):
    if A[i]<0:
        m += 1
    elif A[i]==0:
        z += 1
m = m%2
B = sorted([abs(A[i]) for i in range(N)])
p = m-z
if p>0:
    for i in range(z,z+p):
        B[i] = -B[i]
    print(sum(B))
else:
    print(sum(B))