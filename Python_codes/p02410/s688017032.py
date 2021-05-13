N, M = map(int, input().split())

a = [0]*N
for i in range(N):
  a[i] = list(map(int, input().split()))

b = [0]*M
for i in range(M):
  b[i]= int(input())

c = [0]*N
for i in range(N):
  for aj, bj in zip(a[i], b):
    c[i] += aj * bj
    
for ci in c:
  print(ci)
