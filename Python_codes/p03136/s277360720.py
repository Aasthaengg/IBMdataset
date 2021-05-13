n=int(input())
a=list(map(int,input().split()))

s=sum(a)
if max(a)<s-max(a):
  print('Yes')
else:
  print('No')