str_ = input()
q = int(input())
ss = str_
ans = []
for i in range(q):
  t = input().split(' ')
  if t[0] == 'replace':
    s = ss[0: int(t[1])]
    e = ss[int(t[2]) + 1:len(ss)]
    ss = s + t[3] + e
  elif t[0] == 'reverse':
    s = ss[0: int(t[1])]
    c = ss[int(t[1]):int(t[2]) + 1]
    e = ss[int(t[2]) + 1:len(ss)]
    ss = s + c[::-1] + e
  elif t[0] == 'print':
    ans.append(ss[int(t[1]):int(t[2]) + 1])
for a in ans:
  print(a)
