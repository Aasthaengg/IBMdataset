A, B = map(int,input().split())
count = 0
for i in range(A, B+1):
  x = list(str(i))
  y = x[::-1]
  if x == y:
    count += 1

print(count)   