n = int(input())
a = list(map(int,input().split()))
count = 0
for _ in range(10**6):
  for i in range(n):
    if a[i] % 2 == 0:
      a[i] = a[i]//2
      count += 1
    else:
      break
print(count//n)