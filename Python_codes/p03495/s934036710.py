n, k = map(int, input().split())
alst = list(map(int, input().split()))
alst.sort()
bef = -1
cnt_lst = []
cnt = 0
for a in alst:
  if a == bef:
    cnt += 1
  else:
    cnt_lst.append(cnt)
    cnt = 1
    bef = a
cnt_lst.append(cnt)
ans = 0
l = len(cnt_lst)
cnt_lst.sort()
for i in range(l - k):
  ans += cnt_lst[i]
print(ans)
