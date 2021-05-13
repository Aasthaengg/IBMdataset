n = int(input())
count = 0

for i in range(1,10**10):
  if i**2 <= n:
    count = i**2
  else:
    print(count)
    exit()