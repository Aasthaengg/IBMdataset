inf=998244353


N,K=map(int,input().split())
SS=[list(map(int,input().split())) for i in range(K)]

SS.sort()

table = [0 for k in range(N)] 
diff = [0 for k in range(N-1)]

table[0]=1
diff[0]=-1

for i in range(N-1):
    if table[i]!=0:
        for s in SS:
            lef=s[0]
            rig=s[1]
            if i+lef-1<N-1:
                diff[i+lef-1]+=table[i]
            if i+rig<N-1:
                diff[i+rig]-=table[i]
    table[i+1]=table[i]+diff[i]
    table[i+1]%=inf

print(table[N-1])