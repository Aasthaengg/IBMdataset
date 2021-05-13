N = int(input())
A = list(map(int, input().split()))
A.sort()
p = 1
done = 0

if A[0] == 0:
  print(0)
else:
  for An in A:
    p = p * An
    if p > 10 ** 18:
      print(-1)
      done = 1
      break
  if done == 0:
    print(p)