n = int(input())
a = list(map(int,input().strip().split()))

ordered = [i for i in range(1,n+1)]
i = 0
count = 0

for i in range(n):
  if i == 0:
    if a[i] == ordered[i]:
      tmp = a[i]
      a[i] = a[i+1]
      a[i+1] = tmp
      count += 1
  elif i == n-1:
    if a[i] == ordered[i]:
      tmp = a[i]
      a[i] = a[i-1]
      a[i-1] = tmp
      count += 1  
  else:
    if a[i] == ordered[i]:
      tmp = a[i]
      a[i] = a[i+1]
      a[i+1] = tmp
      count += 1
print(count)