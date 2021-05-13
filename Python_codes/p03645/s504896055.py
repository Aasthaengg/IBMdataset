n,m=map(int,input().split())
A=set()
B=set()

for i in range(m):
  a,b=map(int,input().split())
  if a==1:
    A.add(b)
  if b==n:
    B.add(a)
if len(A&B)==0:
  print("IMPOSSIBLE")
else:
  print("POSSIBLE")

