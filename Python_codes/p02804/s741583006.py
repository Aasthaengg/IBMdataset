n,k=map(int,input().split())
a = list(map(int,input().split()))
di=10**9+7
a.sort()

maxl = a[k-1:]
minl = a[:n-k+1]

kai = [i for i in range(n+1)]
gya = [i for i in range(n+1)]
kai[0]=1
gya[0]=1
for i in range(1,n+1):
    kai[i]=(kai[i-1]*kai[i])%di

for i in range(n+1):
    gya[i]=pow(gya[i],di-2,di)

for i in range(1,n+1):
    gya[i]=(gya[i]*gya[i-1])%di

for i in range(n-k+1):
    tmp=(((kai[k-1+i]*gya[k-1])%di)*gya[i])%di
    maxl[i]=(maxl[i]*tmp)%di

for i in range(n-k+1):
    tmp = (((kai[n-1-i]*gya[k-1])%di)*gya[n-i-k])%di
    minl[i] = (minl[i]*tmp)%di

su=0
for i in range(n-k+1):
    su = (su+maxl[i])%di
    su = (su-minl[i])%di
print(su)
