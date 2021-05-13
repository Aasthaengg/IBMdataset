s = input()
t = input()
les = len(s)
let = len(t)
hoge = 0
if les < let:
  print('UNRESTORABLE')
  exit()
for i in range(les,let-1,-1):
  sa = s[i-let:i]
  for j in range(len(sa)):
    if sa[j] != t[j] and sa[j] != '?':
      break
    if j == len(sa)-1:
      hoge += 1
  if hoge == 1:
    sb = s[:i-let] + t + s[i:]
    ans = ''
    for v in sb:
      if v == '?':
        ans += 'a'
      else:
        ans += v
    print(ans)
    exit()
print('UNRESTORABLE')