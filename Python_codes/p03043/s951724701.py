n,k=map(int,input().split())
d=[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]

coin=[]
for i in range(1,n+1):
  if i>=k:
    coin.append(1)
    continue
  for j in range(19):
    if i*d[j] >= k:
      coin.append(0.5**(j+1))
      break
print(sum(coin)/n)