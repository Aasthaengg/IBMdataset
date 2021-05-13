N=int(input())
a=list(map(int,input().split()))
color=[0]*9
ac=0
for i in range(N):
    rate=min(a[i]//400,8)
    color[rate]+=1
for i in range(8):
    if color[i]>=1:
        ac+=1
min_ans=max(ac,1)
max_ans=ac+color[8]
print(min_ans,max_ans)