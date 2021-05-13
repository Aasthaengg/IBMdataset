M, K = map(int, input().split())

if K >= 2**M:
  print(-1)
elif M == 0:
  print(0,0)
elif M == 1:
  if K == 0:
    print(0,0,1,1)
  elif K == 1:
    print(-1)
else:
  ans = list(range(2**M))
  del ans[K]
  rev = list(reversed(ans))
  ans.append(K)
  ans.extend(rev)
  ans.append(K)
  print(' '.join(map(str, ans)))