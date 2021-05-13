a,b,x = map(int, input().split())
b=b//x + 1
if a!=0:
  a=(a-1)//x + 1
print(b-a)