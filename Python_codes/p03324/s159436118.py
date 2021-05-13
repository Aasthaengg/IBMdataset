d, n = map(int, input().split())
cnt = 0
i = 0
while cnt < n:
  i += 1
  if i % 100**d == 0 and i % 100**(d+1) != 0:
    cnt += 1
print(i)
