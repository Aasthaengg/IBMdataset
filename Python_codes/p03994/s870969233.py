S = input()
K = int(input())
alp = '0bcdefghijklmnopqrstuvwxyza'
alp_dict = {s:i for i,s in enumerate(alp)}


cnt = 0
ans = ''
for i,s in enumerate(S):
  if cnt + (26-alp_dict[s]) <= K:
    cnt += (26-alp_dict[s])
    ans += 'a'
  else:
    ans += s

if (K-cnt)%26==0:
  print(ans)
else:
  rest = (K-cnt)%26
  print(ans[:-1]+alp[(alp_dict[ans[-1]]+rest)%26])