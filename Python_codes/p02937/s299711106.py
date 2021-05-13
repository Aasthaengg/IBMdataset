import bisect
s = list(input())
t = list(input())
n = len(s)
m = len(t)
alphabet = [[] for _ in range(26)]
for i in range(n):
  alphabet[ord(s[i])-ord('a')] += [i] 
loop = 0
pre = -1
for i in range(m):
  c = ord(t[i]) - ord('a')
  if len(alphabet[c]) == 0:
    print(-1)
    exit()
  idx = bisect.bisect_left(alphabet[c], pre+1)
  if idx == len(alphabet[c]):
    loop += 1
    pre = alphabet[c][0]
  else:
    pre = alphabet[c][idx]

print(pre + loop * n + 1)