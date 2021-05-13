X = int(input())
A = 0
for i in range(1, 100000):
  A += i
  if X <= A:
    print(i)
    break