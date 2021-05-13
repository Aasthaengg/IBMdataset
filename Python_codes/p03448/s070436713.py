a, b, c ,x = [int(input()) for i in range(4)]
count = 0
for a in range(a+1):
  for b in range(b+1):
    for c in range(c+1):
      if 500*a + 100*b + 50*c == x:
        count += 1
print(count)