n,x = map(int,input().split())
L = list(map(int,input().split()))
sum = 0
count = 1
for j in range(n):
  sum += L[j]
  if sum <= x:
    count += 1
  else:
    pass
print(count)