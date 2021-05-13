N=int(input())
alist=[0]+list(map(int,input().split()))

answer=0
for i in range(1,N):
  if alist[i]==i:
    alist[i],alist[i+1]=alist[i+1],alist[i]
    answer+=1
    
if alist[N]==N:
  print(answer+1)
else:
  print(answer)