def dfs(str):
    global AGC
    if len(str)==3:
        AGC.append(str)
    else:
        dfs(str+'A')
        dfs(str+'G')
        dfs(str+'C')
        dfs(str+'T')


moji=['A','G','C','T']
AGC=[]
dfs('')
ban=[]
for str in moji:
    ban.append(str+'AGC')
    ban.append(str+'ACG')
    ban.append(str+'GAC')
    ban.append('AGC'+str)
    ban.append('ACG'+str)
    ban.append('GAC'+str)
    ban.append('AG'+str+'C')
    ban.append('A'+str+'GC')

ban=list(set(ban))

N=int(input())
mod=10**9+7
dp=[{key:0 for key in AGC} for i in range(0,N+1)]
for key in AGC:
    if key!='AGC' and key!='ACG' and key!='GAC':
        dp[3][key]=1

for i in range(3,N):
    for key in AGC:
        ans=0
        for str in moji:
            if not key+str in ban:
                dp[i+1][key[1:]+str]+=dp[i][key]

print(sum(dp[N][key] for key in AGC)%mod)