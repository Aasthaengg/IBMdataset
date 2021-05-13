n=int(input())
a=list(map(int,input().split()))
s=set(a)
k=len(s)
if k%2==0:
  print(k-1)
else:
  print(k)