#n=int(input())
n,K=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

pt=set(al)
dic={}
for ai in al:
    dic[ai]=dic.get(ai,0)+1
l2d=[]
for k, v in dic.items():
    l2d.append([k,v])
l2d.sort(key=lambda x: x[1])

ans=0
for i in range(len(pt)-K):
    ans+=l2d[i][1]
print(ans)