N_str = input()
N = int(N_str)
ans = 0
for i in range(len(N_str)):
  cand = 0
  tmp = '9'*i + N_str[i] + '9'*(len(N_str)-i-1)
  if int(tmp) <= N:
    cand = int(tmp)
  else:
    if int(N_str[i]) >= 1:
      tmp = '9'*i + str(int(N_str[i])-1) + '9'*(len(N_str)-i-1)
    if  int(tmp) <= N:
      cand = int(tmp)
  ans = max(ans, sum([int(l) for l in str(cand)]))
print(ans)