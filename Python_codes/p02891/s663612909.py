s = input()
ss = s + s
sss = s + s + s
k = int(input())
n = 0
nn = 0
nnn = 0
s = list(s)
for i in range(1,len(s)):
  if s[i-1] == s[i]:
    n += 1
    s[i] = '.'
ss = list(ss)
for i in range(1,len(ss)):
  if ss[i-1] == ss[i]:
    nn += 1
    ss[i] = '.'
sss = list(sss)
for i in range(1,len(sss)):
  if sss[i-1] == sss[i]:
    nnn += 1
    sss[i] = '.'
a = nn-n*2
if nnn == n*3+a*2:
  print(n*k+a*(k-1))
else:
  print((len(s)*k)//2)