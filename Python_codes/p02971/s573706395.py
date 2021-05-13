N = int(input())
A = [int(input()) for n in range(N)]

sortedA = list(reversed(sorted(A)))
for a in A:
  count = 0
  for b in sortedA:
    if b != a:
      print(b)
      break
    if a == b:
      if count == 0:
        count += 1
      else:
        print(b)
        break