N=int(input())
Z=[0]*N
W=[0]*N

for i in range(N):
  x, y = map(int, input().split())
  Z[i]=x+y
  W[i]=x-y

print(max(max(Z)-min(Z),max(W)-min(W)))