n = int(input())
L = sorted(list(map(int,input().split())))
cnt = 0
for i in range(n):
  for j in range(i):
    for k in range(j):
      if L[i] == L[j]: continue
      if L[j] == L[k]: continue
      if L[k] == L[i]: continue
      if L[k] + L[j] > L[i]:
        cnt += 1
print(cnt)