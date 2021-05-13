N = input()
cnt = 0
ans = 0
for i in range(len(N)):
  if (N[i] == 'A') or (N[i] == 'C') or (N[i] == 'G') or (N[i] == 'T'):
    cnt += 1
    ans = max(cnt, ans)
  else:
    cnt = 0
print(ans)