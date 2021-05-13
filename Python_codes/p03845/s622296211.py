N = int(input())
T = list(map(int,input().split()))

M = int(input())

dic ={}
base = sum(T)

for i in range(M):
  a,b = map(int,input().split())
  print(base - T[a-1]+b)