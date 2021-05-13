A, B, C = map(int, input().split())
T = False
A = A%B
for i in range(1, B+1):
  if A*i%B == C:
    T = True
    break
print("YES" if T else "NO")