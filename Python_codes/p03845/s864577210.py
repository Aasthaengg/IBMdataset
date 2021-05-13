N = int(input())
T = [int(i) for i in input().split()]
M = int(input())

t = sum(T)

for _ in range(M):
  p,x = map(int, input().split())
  print( t - T[p-1] + x)





