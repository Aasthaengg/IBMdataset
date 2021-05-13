import sys
input = sys.stdin.readline
H, W = map(int, input().split())
table = [0] * 26
a = ord("a")
for _ in range(H):
  s = list(input())[: -1]
  for j in range(W):
    table[ord(s[j]) - a] += 1
#print(table)
t = []
for i in range(26):
  if table[i] > 0: t.append(table[i])

x = 0
y = 0
c = 0
if H % 2 and (W % 2):
  c = 1
if H % 2: y += (W - c) // 2
if W % 2: x += (H - c) // 2
#print(x, y, c)
if H > 1 and (W > 1):
  for p in t:
    if p % 2:
      if c > 0:
        c -= 1
        p -= 1
      else:
        print("No")
        exit(0)
    if p % 4:
      if x > 0:
        x -= 1
      elif y > 0:
        y -= 1
      else:
        print("No")
        exit(0)
else:
  for p in t:
    if p % 2:
      if c > 0:
        c -= 1
      else:
        print("No")
        exit(0)
print("Yes")