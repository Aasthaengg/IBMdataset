P = [1 for _ in range(100)]
P[0]=0
P[1]=0
for i in range(2,11):
    for j in range(i*i,100,i):
        P[j] = 0
Q = []
for i in range(100):
    if P[i]==1:
        Q.append(i)
N = int(input())
C = {p:0 for p in Q}
for p in Q:
    cnt = 0
    k = 1
    while p**k<=N:
        for i in range(2,N+1):
            if i%(p**k)==0:
                cnt += 1
        k += 1
    C[p]=cnt
c2=0
c4=0
c14=0
c24=0
c74=0
for p in C:
    if C[p]>=2:
        c2 += 1
    if C[p]>=4:
        c4 += 1
    if C[p]>=14:
        c14 += 1
    if C[p]>=24:
        c24 += 1
    if C[p]>=74:
        c74 += 1
ans = ((c4*(c4-1))//2)*(c2-2)
ans += c24*(c2-1)
ans += c14*(c4-1)
ans += c74
print(ans)