A, B, C = map(int, input().split())
count = 0

while A%2 == 0 and B%2 == 0 and C%2 == 0:
  if A == B and B == C:
    print(-1)
    exit()
  A, B, C = B//2+C//2, A//2+C//2, A//2+B//2
  count += 1
print(count)
  
