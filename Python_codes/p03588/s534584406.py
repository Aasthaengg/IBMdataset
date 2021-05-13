N = int(input())
maxA = 0
minB = 0

for i in range(N):
  a, b = map(int, input().split())
  if(a > maxA):
    maxA = a
    minB = b
  
print(maxA + minB)