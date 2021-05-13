s = list(input())

ans = 0
for i in range(2**(len(s)-1)):
  p = ['']*len(s)
  f = ''
  for j in range(len(s)-1):
    if (i>>j & 1):
      p[j] = '+'
      
  for i in range(len(s)):
    f += s[i] + p[i]
  ans += eval(f)
  
print(ans)