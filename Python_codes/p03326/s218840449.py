N,M=map(int,input().split())
scores=[]
bai=[(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1),(1,-1,-1),(-1,1,-1),\
         (-1,-1,1),(-1,-1,-1)]
scores=[[] for i in range(8)]
for i in range(N):
    a,b,c=map(int,input().split())
    for j in range(8):
        scores[j].append(a*bai[j][0]+b*bai[j][1]+c*bai[j][2])

for i in range(8):
    scores[i].sort(reverse=True)

ans=0
for i in range(8):
    ans=max(ans,sum(scores[i][:M]))
print(ans)
