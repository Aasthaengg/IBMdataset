N,K,C=map(int,input().split())
S=input()

maekara=[]
i=1
cnt=0
while i<=N and cnt<K:
    if S[i-1]=='o':
        maekara.append(i)
        i+=C+1
        cnt+=1
    else: i+=1

usirokara=[]
j=N
cnt=0
while j>=1 and cnt<K:
    if S[j-1]=='o':
        usirokara.append(j)
        j-=C+1
        cnt+=1
    else: j-=1
usirokara=usirokara[::-1]

for i in range(K):
    if maekara[i]==usirokara[i]:
        print(maekara[i])
