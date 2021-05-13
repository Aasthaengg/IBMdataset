x = list(map(int, input().split()))
cnt = 0
for i in range(x[0]+1):
  for j in range(x[0]+1):
    p = i+j
    if (p <= x[1]) and (x[0]+p) >= x[1]:
      cnt += 1
print(cnt)