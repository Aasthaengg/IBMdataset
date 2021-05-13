N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
num = 1

while num <= N:
  D = D + L[num-1]
  if D > X:
    print(num)
    break
  num += 1
else:
  print(N+1)