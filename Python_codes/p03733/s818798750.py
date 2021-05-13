N, T = map(int,input().split())

TL = list(map(int,input().split()))

ans = 0

for i in range(N-1):
  stop = TL[i] + T
  if stop >= TL[i+1]:
    ans += TL[i+1]-TL[i]
  else:
    ans += T
ans += T
print(ans)