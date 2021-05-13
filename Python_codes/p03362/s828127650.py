#17:30
n = int(input())
i = 11
cnt = 0
ans = []
while cnt < n:
  for j in range(2,int(i**.5)+1):
    if i % j == 0:
      i += 10
      break
  else:
    cnt += 1
    ans.append(i)
    i += 10
print(' '.join(list(map(str,ans))))