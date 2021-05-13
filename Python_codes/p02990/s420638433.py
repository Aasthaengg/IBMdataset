N,K=list(map(int,input().split()))
mod=10**9+7

red=N-K
blue=K

place=red+1

combp=[1]*(place+1)
combb=[1]*(blue)

def invmod(x):
    return pow(x,mod-2,mod)

for r in range(1,place+1):
    combp[r]=(combp[r-1]*(place-r+1)*invmod(r))%mod

for r in range(1,blue):
    combb[r]=(combb[r-1]*(blue-r)*invmod(r))%mod

for i in range(1,K+1):

    if place<i:
        print(0)
        continue

    print((combp[i]*combb[i-1])%mod)