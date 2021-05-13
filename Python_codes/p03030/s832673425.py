N = int(input())
SP = [list(input().split()) + [i + 1] for i in range(N)]

for i in range(N):
  SP[i][1] = -int(SP[i][1])

SP.sort()

for i in range(N):
  print(SP[i][2])