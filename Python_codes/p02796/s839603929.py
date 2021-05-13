n=int(input())
xlr=[[] for _ in range(n)]

for i in range(n):
    xx,ll = map(int,input().split())
    xlr[i] = [xx,ll,xx-ll,xx+ll]
    
xlr.sort(key = lambda x:x[3])

ans=1
right=xlr[0][-1]
for i in range(1,n):
    if right <= xlr[i][2]:
        ans+=1
        right=xlr[i][-1]

print(ans)