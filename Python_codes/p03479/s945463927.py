x, y = map(int, input().split())
A = [x]
while True:
  a = 2 * A[-1]
  if a > y:
    break
  A.append(a)
print(len(A))