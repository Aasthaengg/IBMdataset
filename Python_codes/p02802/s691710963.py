N,M = map(int,input().split())
ac_cnt = [0] * (N + 1)
wa_cnt = [0] * (N + 1)

for i in range(M):
  p,S = input().split()
  p = int(p)
  
  if ac_cnt[p] == 0:
    if S == "WA":
      wa_cnt[p] += 1
    else:
      ac_cnt[p] += 1
    
wa_cnt = [wa for i, wa in enumerate(wa_cnt) if ac_cnt[i] == 1]
print(sum(ac_cnt),sum(wa_cnt))