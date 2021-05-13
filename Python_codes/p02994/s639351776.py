n,l=map(int,input().split())
a=list(range(l,l+n,1))
x=sum(a)
if(0 in a):
  a.remove(0)
  print(sum(a))
elif(x<0):
  a.remove(max(a))
  print(sum(a))
elif(x>0):
  a.remove(min(a))
  print(sum(a))