n=int(input())
b=[0]*(n+1)
for p in (int(input()) for _ in range(n)):
  b[p]=b[p-1]+1
print(n-max(b))