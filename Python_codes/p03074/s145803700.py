from collections import deque
n,k=map(int,input().split())
s=list(map(int,list(input())))
cnt=0
q=deque()
prev=1
ans=[]
for i in s:
    if i==0 and prev==1:
        cnt+=1
    q.append(i)
    prev=i
    if cnt>k:
        #print(q)
        ans.append(len(q)-1)
        prev1=1
        while len(q)>0:
            if q[0]==1 and prev1==0 and cnt<=k:
                break
            if q[0]==0 and prev1==1:
                cnt-=1
            prev1=q[0]
            q.popleft()
ans.append(len(q))
print(max(ans))