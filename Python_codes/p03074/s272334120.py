from itertools import accumulate

N,K=map(int,input().split())
S=input()

count=[0]
if S[0]=="0":
    count.append(0)

s=S[0]
cnt=0
for i in range(N):
    if s==S[i]:
        cnt+=1
    else:
        count.append(cnt)
        cnt=1
        s=S[i]
count.append(cnt)
if S[N-1]=="0":
    count.append(0)

l=len(count)
count=list(accumulate(count))
ans=0
for i in range(0,l,2):
    ans=max(ans,count[min(l-1,i+2*K+1)]-count[i])
print(ans)