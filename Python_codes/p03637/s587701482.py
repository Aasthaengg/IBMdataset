n=int(input())
x=list(map(int,input().split()))
a,b,c=0,0,0
ans='No'
for i in x:
  if i%4==0:
    a+=1
  elif i%2==0:
    b+=1
  else:
    c+=1
if n%2==1:
  if c-a==1:
    if b==0:
      ans='Yes'
  elif a>=c:
    ans='Yes'
else:
  if a>=c:
    ans='Yes'
print(ans)
