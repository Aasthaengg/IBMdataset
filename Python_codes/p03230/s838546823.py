N = int(input())
flg = 0
k = 0
while k * (k - 1) <= 2 * N:
  if k * (k - 1) == 2 * N:
    flg = 1
    break
  else:
    k += 1
if flg == 0:
  print("No")
else:
  print("Yes")
  print(k)
  S = [[k-1] for _ in range(k)]
  cnt = 1
  for i in range(k-1):
    for j in range(i+1, k):
      S[i].append(cnt)
      S[j].append(cnt)
      cnt += 1
  for i in range(k):
    for j in range(k):
      if j == k:
        print(S[i][j])
      else:
        print(S[i][j], end = ' ')
    print()