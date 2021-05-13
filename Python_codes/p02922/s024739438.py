A,B = map(int, input().split())
for i in range(10**10 + 1):
  C = 1 + (A-1) * i
  if B <= C:
    print(i)
    break
