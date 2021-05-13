n, k = map(int, input().split()) 

if 2 * k > (n-1) * (n-2):
  print(-1)
else:
  ans = [(1, i) for i in range(2, n+1)]
  p =  (n-1) * (n-2) // 2
  i = 2
  j = 3
  while p > k:
    ans.append((i, j))
    p -= 1
    j += 1
    if j == n + 1:
      i += 1
      j = i + 1
  print(len(ans))
  for a in ans:
    print(" ".join(map(str, a)))