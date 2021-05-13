n=int(input())
t,a=[0]*n,[0]*n
for i in range(n):
  t[i],a[i]=map(int,input().split())
tt,aa=t[0],a[0]
for i in range(1,n):
  tt=t[i]*max((tt+t[i]-1)//t[i],(aa+a[i]-1)//a[i])
  aa=a[i]*max((tt+t[i]-1)//t[i],(aa+a[i]-1)//a[i])
print(aa+tt)