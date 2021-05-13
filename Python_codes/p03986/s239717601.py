X = input()

s_cnt = 0
t_cnt = 0

ans = 0

for n in range(len(X)):
  if X[n] == "S":
    s_cnt += 1
  else:
    t_cnt += 1
  ans = max(ans,t_cnt-s_cnt)
print(ans*2)