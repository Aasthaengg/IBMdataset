N = int(input())
D = input().split(' ')
D = [int(D[i]) for i in range(N)]
D = sorted(D)
if not N%2 == 0:
  print(0)
else:
  print(D[int(N/2)] - D[int(N/2) - 1])