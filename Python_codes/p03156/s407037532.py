n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
ta=0
tb=0
tc=0
for i in range(n):
  if p[i]<=a:
    ta=ta+1
  elif p[i]>=b+1:
    tc=tc+1
  else:
    tb=tb+1
print(min(ta,tb,tc))