n=int(input())
mod=10**9+7
if n==3:
    print(61)
    exit()
zt=['A','G','C','T']
for i in range(3):
    tmp=[]
    for j in zt:
        for k in list('AGCT'):
            tmp.append(j+k)
    zt=tmp
ng=set([])
for i in list('AGCT'):
    ng.add('AGC'+i)
    ng.add('AG'+i+'C')
    ng.add('A'+i+'GC')
    ng.add(i+'AGC')
    ng.add('ACG'+i)
    ng.add('GAC'+i)
    ng.add(i+'ACG')
    ng.add(i+'GAC')
z=[]
for j in zt:
    if not j in ng:
        z.append(j)
zn=len(z)
dp=[[0 for j in range(zn)] for i in range(n-3)]
for i in range(zn):
   # if not z[i] in ng:
    dp[0][i]=1
for i in range(n-4):
    for j in range(zn):
        for k in range(zn):
            #if not z[k] in ng:
            if z[j][1:]==z[k][:3]:
                dp[i+1][k]+=dp[i][j]
                dp[i+1][k]%=mod
print(sum(dp[-1])%mod)
