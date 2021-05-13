s = list(input())
t = list(input())
s.sort()
t.sort()
t.reverse()
S=len(s)
T=len(t)
x = set(s)
y = set(t)
n = min(S, T)


for i in range(n):
  if ord(s[i]) > ord(t[i]):
    print('No')
    exit()
  elif ord(s[i]) < ord(t[i]):
    print('Yes')
    exit()
    
if x==y:
  if S<T:
    print('Yes')
    exit()
  else:
    print('No')
    exit()