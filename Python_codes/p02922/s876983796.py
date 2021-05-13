a,b = map(int,input().split())
if (b-1)%(a-1)==0:
  n= (b-1)/(a-1)
else:
  n= (b-1)//(a-1)+1
print(int(n))