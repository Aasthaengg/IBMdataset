n = int(input())
a = list(map(int,input().split()))
i = 0
mae = 0
c = 0
while i < n:
  if mae == a[i]:
    c += 1
    mae = 0
  else:
    mae = a[i]
  i += 1
print(c)