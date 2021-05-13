a,b = map(int,input().split())
max = a+b
if max < a-b:
  max = a-b
if max < a*b:
  max = a*b
print(max)