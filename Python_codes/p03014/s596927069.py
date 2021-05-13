h, w = map(int, input().split())
s = []
for i in range(h):
  t = input()
  s.append(t)
yokol = [[0 for i in range(w)] for j in range(h)]
yokor = [[0 for i in range(w)] for j in range(h)]
tateu = [[0 for i in range(w)] for j in range(h)]
tated = [[0 for i in range(w)] for j in range(h)]

for i in range(h):
  cnt = 0
  for j in range(w):
    if s[i][j] == '#':
      cnt =0
    else:
      cnt += 1
      yokol[i][j] = cnt
  cnt = 0
  for j in reversed(range(w)):
    if s[i][j] == '#':
      cnt=0
    else:
      cnt += 1
      yokor[i][j] = cnt

for j in range(w):
  cnt = 0
  for i in range(h):
    if s[i][j] == '#':
      cnt =0
    else:
      cnt += 1
      tateu[i][j] = cnt
  cnt = 0
  for i in reversed(range(h)):
    if s[i][j] == '#':
      cnt =0
    else:
      cnt += 1
      tated[i][j] = cnt

ans = 0
for i in range(h):
  for j in range(w):
    x = yokol[i][j] + yokor[i][j] + tateu[i][j] + tated[i][j] - 3
    ans = max(ans,x)
print (ans)