N = int(input())
X = list(map(int, input().split()))
P = sum(X) // N
result1 = 0
result2 = 0

for x in X:
  result1 += (x - P)**2
  result2 += (x - P - 1)**2

if result1 <= result2:
  result = result1
elif result1 > result2:
  result = result2


print(result)