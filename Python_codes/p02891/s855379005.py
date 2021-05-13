s = input()
t = int(input())
v = set(s)

ans = 0
if len(v) == 1:
  ans = (len(s)*t)//2
  print (ans)
  exit()

a = []
o = s[0]
c = 0

for i in range(len(s)):
  if o == s[i]:
    c += 1
  else:
    a.append([o,c])
    c = 1
    o = s[i]
a.append([o,c])

for i,j in a:
  if j == 1:
    continue
  ans += (j//2)*t

if len(v) > 1:
  if a[0][0] == a[-1][0]:
    if a[0][1]%2 == 1 and a[-1][1]%2 == 1:
      ans += t-1

print (ans)