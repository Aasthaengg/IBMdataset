N,K=map(int,input().split())
num = [0]*(int(1e5)+1)
for _ in range(N):
  a,b=map(int,input().split())
  num[a] += b
for i in range(int(1e5)+1):
  K -= num[i]
  if K <= 0:
    print(i)
    break