S = str(input())

_sum = 0
ans = 0

for s in S:
  
  if s == "B":
    _sum += 1
    
  elif s == "W":
    ans += _sum
    
print(ans)