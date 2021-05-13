a, b, x = map(int, input().split())

c=b//x
if a%x==0:
  d=a//x-1
else:
  d=a//x
print(c-d)