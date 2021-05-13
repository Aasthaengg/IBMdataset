N=int(input())
T = list(map(int, input().strip().split()))
M = int(input())

total = sum(T)

for i in range(M):
  p,x = list(input().strip().split())
  p = int(p)
  x = int(x)
  print(total - T[p-1] + x)