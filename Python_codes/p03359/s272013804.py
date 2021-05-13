a,b = map(int, input().split())

before = a - 1
now = 0
if a <= b:
  now = 1
  
print(before + now)