N=int(input())
alist=[0]+list(map(int,input().split()))

answer=0
if alist[N]==N:
  alist[N-1],alist[N]=alist[N],alist[N-1]
  answer+=1

for i in range(1,N+1):
  if alist[i]==i:
    alist[i],alist[i+1]=alist[i+1],alist[i]
    answer+=1
    
print(answer)