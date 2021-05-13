a = list(map(int,input().split()))
max = -10 ** 25
for i in range(2):
  for j in range(2,4):
    p = a[i] * a[j]
    if max < p:
      max = p
print(max)