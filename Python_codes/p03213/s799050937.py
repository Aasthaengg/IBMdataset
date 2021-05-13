P = [1 for _ in range(100)]
P[0]=0
P[1]=0
for i in range(2,11):
    for j in range(i*i,100,i):
        P[j] = 0
Q = []
for i in range(2,100):
    if P[i]==1:
        Q.append(i)
C = {q:0 for q in Q}
N = int(input())
for i in range(2,N+1):
    x = i
    for q in Q:
        while x%q==0:
            x = x//q
            C[q] += 1
D = {2:0,4:0,14:0,24:0,74:0}
for q in Q:
    if C[q]>=2:
        D[2] += 1
    if C[q]>=4:
        D[4] += 1
    if C[q]>=14:
        D[14] += 1
    if C[q]>=24:
        D[24] += 1
    if C[q]>=74:
        D[74] += 1
cnt = D[74]
cnt += (D[2]-D[24])*D[24]+(D[24]*(D[24]-1))
cnt += (D[4]-D[14])*D[14]+(D[14]*(D[14]-1))
cnt += (D[2]-D[4])*(D[4]*(D[4]-1))//2+(D[4]*(D[4]-1)*(D[4]-2))//2
print(cnt)