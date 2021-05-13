# do simulation

X = int(input())
Y, K = 0, 0
while True:
  Y += X
  K += 1
  if Y % 360 == 0:
    print(K)
    exit()