a = int(input())
b = int(input())
ans = 'GREATER'
if a == b:
  ans = 'EQUAL'
elif a < b:
  ans = 'LESS'
print(ans)