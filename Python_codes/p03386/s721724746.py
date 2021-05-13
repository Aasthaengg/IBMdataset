A, B, K = map(int, input().split())
ans1 = set()
ans2 = set()
for i in range(A, B + 1):
  if len(ans1) < K:
    ans1.add(i)
  else:
    break
    
for i in reversed(range(A, B + 1)):
  if len(ans2) < K:
    ans2.add(i)
  else:
    break

ans = ans1 | ans2
for a in sorted(list(ans)):
  print(a)