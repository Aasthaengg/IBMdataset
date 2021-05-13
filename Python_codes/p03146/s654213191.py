N = int(input())
l = [N]
ans = 0
while True:
  if N % 2 == 0:
    N /= 2
  else:
    N = 3 * N + 1
  if N in l:
    print(len(l) + 1)
    break
  l.append(N)