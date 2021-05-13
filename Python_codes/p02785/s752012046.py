N,K = map(int,input().split())
Hli = list(map(int,input().split()))

Hli.sort(reverse = True)
res = 0

for i in range(K,N):
  res += Hli[i]

print(res)