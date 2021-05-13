N = int(input())
L = [int(l) for l in input().split(" ")]

def solve():
  ans = 0
  if len(L) < 3:
    return 0
  for i in range(N):
    for j in range(i, N):
      for k in range(j, N):
        if L[i] != L[j] and\
           L[j] != L[k] and\
           L[k] != L[i]:
          d = {i: L[i], j:L[j], k:L[k]}
          max_idx = max(d, key=lambda x: d[x])
          if sum(d.values()) - 2*L[max_idx] > 0:
            ans += 1# .append((i,j,k))
  return ans

print(solve())