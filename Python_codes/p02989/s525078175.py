n=int(input())
d=list(map(int,input().split()))
d.sort()
s=n//2-1
a=d[s]
b=d[s+1]
if a==b:
  print(0)
  
else:
  print(b-a)