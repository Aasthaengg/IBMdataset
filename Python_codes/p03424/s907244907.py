N=int(input())
S=list(input().split())
X=set()
for s in S:
  X.add(s)
  
if len(X)==3:
  print('Three')
else:
  print('Four')
