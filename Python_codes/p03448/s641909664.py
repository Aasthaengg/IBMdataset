a=int(input())
b=int(input())
c=int(input())
x=int(input())
ans=0
for i in range(a+1):
  A=500*i
  if A>x:
    break
  for j in range(b+1):
    B=100*j
    k = (x - A - B)/50
    if 0<=k<=c and k%1==0:
      ans+=1
print(ans)