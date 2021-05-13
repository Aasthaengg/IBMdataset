N,K=map(int,input().split())
td=[list(map(int,input().split())) for _ in range(N)]
td=[[td[i][0]-1,td[i][1]] for i in range(N)]

hozon_a=[[] for _ in range(N)]
hozon_b=[[] for _ in range(N)]

td.sort(key=lambda x:x[1],reverse=True)
for i in range(K):
    hozon_a[td[i][0]].append(td[i][1])
for i in range(K,N):
    if hozon_a[td[i][0]]==[] and hozon_b[td[i][0]]==[]:
        hozon_b[td[i][0]].append(td[i][1])

cnt=len([None for a in hozon_a if a!=[]])
ans=sum([sum(hozon_a[i]) for i in range(N)])+cnt**2

hozon_aa=[hozon_a[i][1:] for i in range(N) if len(hozon_a[i])>1]
hozon_aa=[e for inner_list in hozon_aa for e in inner_list]
hozon_bb=[hozon_b[i][0] for i in range(N) if hozon_b[i]!=[]]

hozon_aa.sort(reverse=True)
hozon_bb.sort(reverse=False)

cnt1=cnt
temp=ans
for i in range(min(K-cnt,len(hozon_aa),len(hozon_bb))):
    temp+=hozon_bb.pop()-hozon_aa.pop()+2*cnt1+1
    cnt1+=1
    if ans<temp:
        ans=temp
print(ans)