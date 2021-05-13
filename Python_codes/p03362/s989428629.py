INF = 55555
P = [1 for _ in range(55556)]
P[0]=0
P[1]=0
for i in range(2,int(55556**0.5)+1):
    for j in range(i*i,55556,i):
        P[j] = 0
N = int(input())
A = []
for i in range(11,55556,10):
    if P[i]==1:
        A.append(i)
    if len(A)==N:
        break
print(*A)