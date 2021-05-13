a,b,c=map(int,input().split())
d=b//a
if (d+1)*a<=b:
  d+=1
print(min(d,c))