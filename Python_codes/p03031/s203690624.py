n,m = map(int,input().split())
ans = 0
Lamp_switch = []
for _ in range(m):
    S = list(map(int, input().split()))[1:]
    Lamp_switch.append(S)
Pon = list(map(int, input().split()))

for i in range(2**n):
  cnt = [0]*m
  for j in range(n):
    if (i>>j)&1:
      for k in range(m):
        if (j+1) in Lamp_switch[k]:
          cnt[k] += 1
          cnt[k] %= 2
  if cnt == Pon:
    ans += 1
    
print(ans)