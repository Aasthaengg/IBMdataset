P = [1 for _ in range(100)]
P[0]=0
P[1]=0
for i in range(2,10):
    for j in range(i*i,100,i):
        P[j] = 0
Q = []
for i in range(100):
    if P[i]==1:
        Q.append(i)
C = {i:0 for i in Q}
N = int(input())
for i in range(2,N+1):
    x = i
    for p in C:
        while x%p==0:
            x = x//p
            C[p] += 1
#2 4 4
c2 = 0
c4 = 0
for p in C:
    if 2<=C[p]<4:
        c2 += 1
    elif C[p]>=4:
        c4 += 1
cnt = c2*((c4*(c4-1))//2)+c4*(((c4-1)*(c4-2))//2)
#2 24
c2 = 0
c24 = 0
for p in C:
    if 2<=C[p]<24:
        c2 += 1
    elif C[p]>=24:
        c24 += 1
cnt += c2*c24+c24*(c24-1)
#4 14
c4 = 0
c14 = 0
for p in C:
    if 4<=C[p]<14:
        c4 += 1
    elif C[p]>=14:
        c14 += 1
cnt += c4*c14+c14*(c14-1)
#75
c74 = 0
for p in C:
    if C[p]>=74:
        c74 += 1
cnt += c74
print(cnt)