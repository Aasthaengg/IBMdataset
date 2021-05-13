n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A) < sum(B):
  print(-1)
else:
  diffs = [a - b for a, b in zip(A, B)]
  diffs.sort()
  changed = set()
  l = 0
  r = n - 1
  while l < r:
    if diffs[l] >= 0:
      break
    if diffs[r] + diffs[l] == 0:
      changed.add(l)
      changed.add(r)
      l += 1
      r -= 1
    elif diffs[r] + diffs[l] > 0:
      changed.add(l)
      changed.add(r)
      diffs[r] += diffs[l]
      l += 1
    else:
      changed.add(l)
      changed.add(r)
      diffs[l] += diffs[r]
      r -= 1
  print(len(changed))      
