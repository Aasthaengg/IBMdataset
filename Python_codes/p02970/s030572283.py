N, D = map(int, input().split())
R = 0
for i in range(1,N+1):
  R += 2 * D + 1
  if N <= R:
    print(i)
    exit()