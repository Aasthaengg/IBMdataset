n,c,k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()

T = 0
cnt = 0
ans = 0
for i in range(n):
  if cnt == 0: #誰も待っていない
    T = t[i] + k
    cnt += 1
  elif t[i] <= T:
    cnt += 1
  elif t[i] > T:
    ans += 1
    cnt = 1
    T = t[i] + k
  if cnt == c:
    ans += 1
    T = 0
    cnt = 0
if cnt != 0: ans += 1
print(ans)