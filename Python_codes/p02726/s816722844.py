n,x,y=map(int,input().split())
 
ans=[0]*n
 
list =[]
for i in range(n):
  for j in range(i):
    b = i+1
    a = j+1
    if a<=x and b>=y:
      k =b-y+x-a+1
    elif a>x and b>=y:
      d =min(a-x+1,y-a)
      k =d+b-y
    elif a<=x and b<y:
      d =min(b-x,y-b+1)
      k =x-a+d
    elif a>x and b<y:
      k = min(b-a,y-b+a-x+1)
    ans[k]+=1
    
for i in range(1,n):
  print(ans[i])