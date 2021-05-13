n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
ans =  10**6
for i in range(4**n):
  s = Base_10_to_n(i, 4)
  s = s.zfill(n)
  l_temp = [0, 0, 0]
  cnt = [0, 0, 0]
  for num, j in enumerate(s):
    if int(j):
      l_temp[int(j)-1] += l[num]
      cnt[int(j)-1] += 1
  if 0 in cnt:
    continue
  else:
    ans_temp = 10*(sum(cnt)-3) +abs(A-l_temp[0]) + abs(B-l_temp[1]) + abs(C-l_temp[2])
    ans = min(ans, ans_temp) 
print(ans)