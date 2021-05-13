#from statistics import mean, median,variance,stdev
a,b,c=map(int, input().split())

x=min(a,b,c)
z=max(a,b,c)
if a==x and b==z:
  y=c
if a==x and c==z:
  y=b
if b==x and a==z:
  y=c
if b==x and c==z:
  y=a
if c==x and a==z:
  y=b
if c==x and b==z:
  y=a

print(0 if z%2==0 else x*y)