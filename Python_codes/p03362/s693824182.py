n = int(input())

Nmax = 55555
f = [-1 for i in range(Nmax)]

for i in range(2,Nmax):
    if f[i]==-1:
        f[i]=True
        for j in range(i+i,Nmax,i):
            f[j] = False

f[0]=False
f[1]=False
lis = []
for i in range(1,6000):
    nu = i*10+1
    if nu<=Nmax and f[nu]==True:
        lis.append(nu)

    if len(lis)>=n:
        break

print(*lis)
