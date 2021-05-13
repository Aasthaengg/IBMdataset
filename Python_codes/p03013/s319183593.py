import time
MOD = 10**9+7

n,m = map(int,input().split())

stime = time.time()
F=[0]*(n+1)
F[0]=1
F[1]=2
for i in range(2,n):
    F[i]=(F[i-1]+F[i-2])%MOD

etime =time.time()


a=[0]*(n+1)
ans=1
for i in range(m):
      a[int(input())-1]+=1

io=-1
for i in range(n-1):
      if 0!=a[i] :
            io=i+1
            if 0!=a[i+1]:
                  print("0")
                  exit()
      else:
            if a[i+1] and i-io>1 :
                  ans*=F[i-io-1]%MOD
                  s=0
i=n-1
if i-io>0 :
      ans*=F[i-io-1]%MOD
print(ans%MOD)      
