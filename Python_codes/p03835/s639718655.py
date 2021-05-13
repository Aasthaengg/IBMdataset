K,S=map(int,input().split())
c = 0
res = 0
for i in range(K+1):
  for j in range(K+1):
    c = S-i-j
    if 0<=c<=K:
      res += 1
print(res)