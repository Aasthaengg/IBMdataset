import collections
N = int(input())
D = collections.Counter(list(map(int, input().split())))
M = int(input())
T = collections.deque(sorted(list(map(int, input().split()))))
ans = 'YES'
for i in range(M):
  prb = T.pop()
  #print(prb, D)
  if prb in D:
    if D[prb]:
      D[prb] -= 1
      if not D[prb]:
        del D[prb]
    else:
      ans = 'NO'
      break
  else:
    ans = 'NO'
    break
print(ans)
