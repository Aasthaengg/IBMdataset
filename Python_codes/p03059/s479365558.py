A, B, T = map(int, input().split())
time = A
T += 0.5
biscuit = 0
while A < T:
  biscuit += B
  A += time
print(biscuit)