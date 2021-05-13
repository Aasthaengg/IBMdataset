import bisect
s = input()
l = len(s)
ch = [[] for _ in range(26)]
s *= 2
for i in range(l*2):
  ch[ord(s[i]) - ord("a")].append(i)
  
t = input()
ans = 0
now = -1
for i in t:
  idx = ord(i) - ord("a")
  if not ch[idx]:
    print(-1)
    break
  temp = bisect.bisect_right(ch[idx], now)
  ans += ch[idx][temp] - now
  now = ch[idx][temp]%l
else:
  print(ans)