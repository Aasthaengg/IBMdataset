def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
P = [1 for _ in range(10**6)]
P[0]=0
P[1]=0
for i in range(2,10**3):
    for j in range(i*i,10**6,i):
        P[j] = 0
Q = []
for i in range(2,10**6):
    if P[i]==1:
        Q.append(i)
A,B = map(int,input().split())
N = gcd(A,B)
R = [1]
for p in Q:
    if N%p==0:
        R.append(p)
        while N%p==0:
            N = N//p
if N>1:
    R.append(N)
print(len(R))