N=int(input())

maxn=55555

prime=[1]*(maxn+1)
prime[0]=0
prime[1]=0
plst=[]
for i in range(2,maxn+1):
    if prime[i]==1:
        if i%5==1:
            plst.append(str(i))
        for j in range(2,maxn//i+1):
            prime[i*j]=0

print(' '.join(plst[:N]))