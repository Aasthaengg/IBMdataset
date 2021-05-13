N,x=map(int,input().split())
alist=list(map(int,input().split()))

answer=0
if alist[0]>x:
  answer+=alist[0]-x
  alist[0]=x
  
for i in range(1,N):
  if alist[i-1]+alist[i]>x:
    answer+=alist[i-1]+alist[i]-x
    alist[i]=x-alist[i-1]
    
#print(alist)
print(answer)