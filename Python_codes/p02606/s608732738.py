l, r, d = map(int, input().split())

result = 0
for x in range(l, r+1):
  if x % d == 0:
    result += 1
  
print(result)