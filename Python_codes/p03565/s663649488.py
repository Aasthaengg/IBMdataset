s = '.'+input()+'.'
t = input()
def onazi(a):
  for i in range(len(t)):
    if a[i] == '?':
      continue
    if a[i] != t[i]:
      return 0
  return 1
cnt=0
for i in range(len(s)-len(t),0,-1):
  if onazi(s[i:i+len(t)])==1:
    cnt+=1
    s = s[:i]+t+s[i+len(t):]
    break
if cnt==0:
  print('UNRESTORABLE')
  exit(0)
g = ''
for i in s[1:-1]:
  if i == '?':
    g+='a'
  else:
    g+=i
print(g)