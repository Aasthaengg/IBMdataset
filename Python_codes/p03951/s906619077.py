N = int(input())
s = input()
t = input()
ans=maxlen=len(s)+len(t)

for i in range(len(s)):
  if len(s[i:]) <= len(t):
    complen = len(s[i:])
    if maxlen-complen>=N and s[i:] == t[0:complen]:
      ans=maxlen-complen
      break
      
      
print(ans)