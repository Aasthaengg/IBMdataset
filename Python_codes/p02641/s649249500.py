x,n=map(int,input().split())
if n==0:
  p=set()
else:
  p=set(map(int,input().split()))

for i in range(1000):
  if x-i not in p:
    print(x-i)
    break
  elif x+i not in p:
    print(x+i)
    break
