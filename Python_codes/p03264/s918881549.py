k = int(input())
cnt = 0
for i in range(1,k+1):
  for j in range(i+1,k+1):
    if (i % 2 == 0 and j % 2 == 1) or (j % 2 == 0 and i % 2 == 1):
      cnt += 1

print(cnt)