a,b,c = map(int, input().split())
max_value = a
if b > max_value:
  max_value = b
if c > max_value:
  max_value = c
  
print(a + b + c - max_value)