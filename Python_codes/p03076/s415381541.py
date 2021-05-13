A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
a=[0]*5
a[0]=A
a[1]=B
a[2]=C
a[3]=D
a[4]=E
b=[0]*5
for x in range(5):
  if a[x]%10!=0:
    b[x]=a[x]%10
  else:
    b[x]=10
t=min(b)
ti=b.index(t)
ans=0
for i in range(5):
  if i!=ti:
    if a[i]%10!=0:
      ans+=a[i]+(10-a[i]%10)
    else:
      ans+=a[i]
ans+=a[ti]
print(ans)
