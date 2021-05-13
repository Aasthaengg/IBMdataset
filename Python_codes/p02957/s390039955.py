# abs(a-k)==abs(b-k)
# a-k+b-k=0 or a-k-b+k=0
# a!=bから左
# a+b==2k

a,b=map(int,input().split())

c=a+b

if c%2==1:
  print("IMPOSSIBLE")
else:
  print(c//2)