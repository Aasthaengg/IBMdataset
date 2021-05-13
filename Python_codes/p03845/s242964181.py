N = int(input())
T = [int(i) for i in input().split()]
T_SUM = sum(T)
M = int(input())
PX = [tuple(map(int,input().split())) for _ in range(M)]
for px in PX:
  time = T_SUM + px[1] - T[px[0]-1]
  print(time)