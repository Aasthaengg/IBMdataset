from collections import Counter
H, W = map(int, input().split())
s = ''
for i in range(H):
  s += str(input())
  
c = Counter(s)
m = c.most_common()
cnt = 0
l = []
for n in m:
  cnt += n[1] // 4
  l.append(n[1]%4)
if cnt < (H//2)*(W//2):
  print('No')
else:
  cnt = 0
  for i in l:
    if i % 2 == 1:
      cnt += 1
  if cnt <= 1:
    print('Yes')
  else:
    print('No')