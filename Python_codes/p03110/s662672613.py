N=int(input())
D={'JPY':1, 'BTC':380000}
a=0
for _ in range(N):
  v,s=list(input().split())
  a+=float(v)*D[s]
print(a)