def check(w,k,mid):
  weight=mid
  remains=k
  flag=True
  for i in range(len(w)):
    if weight>=w[i]:
      weight-=w[i]
    else:
      remains-=1
      if remains==0:
        flag=False
        break
      weight=mid
      weight-=w[i]

  return flag



n,k=map(int,input().split())
w=[]

for i in range(n):
  a=int(input())
  w.append(a)

left=max(w)
right=sum(w)
mid=0

while(1):
  mid=int((left+right)/2)
  #print(left,mid,right)
  if check(w,k,mid):
    right=mid
  else:
    left=mid+1

  if left>=right:
    print(left)
    break
