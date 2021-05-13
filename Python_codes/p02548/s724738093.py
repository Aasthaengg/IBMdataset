N = int(input())
count = 0
for a in range(1,N+1):
  for b in range(a,N//a+1):
    if a * b < N:
      if a == b:
        count += 1
      else:
        count += 2
print(count)