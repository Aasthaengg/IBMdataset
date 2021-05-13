N, K = map(int,input().split())

for i in range(N):
  if i==0:
    pat = K
  else:
    pat = pat * (K - 1)

print(pat)
