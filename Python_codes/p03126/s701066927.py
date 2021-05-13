N,M = map(int,input().split())
like = [1]
for i in range(2,M+1):
  like.append(i)
for j in range(N):
  A = list(map(int,input().split()[1:]))
  for l in range(M):
    if l+1 in A:
      continue
    else:
      if l+1 in like:
        like.remove(l+1)
print(len(like))