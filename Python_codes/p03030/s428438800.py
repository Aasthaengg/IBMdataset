N=int(input())
S=[[] for i in range(N)]
for i in range(N):
    s,p=map(str,input().split())
    S[i]=[s,int(p)*(-1),i]

S.sort(key=lambda x:(x[0],x[1]))

for i in range(N):
    print(S[i][2]+1)