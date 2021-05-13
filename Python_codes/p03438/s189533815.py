N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = [a - b for a, b in zip(A, B)]
diff.sort()
k = 0
for d in diff:
  if d < 0:
    if d % 2 == 0:
      k += -d // 2
    else:
      k += -(d+1) // 2
  elif d == 0:
    continue
  else:
    k -= d

print(['Yes', 'No'][k<0])