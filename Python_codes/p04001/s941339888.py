s = input()
n = len(s)-1
total=0
for i in range(2**n):
  pl=['']*n
  ans=''
  for j in range(n):
    if ((i>>j)&1):
      pl[n-1-j] = '+'
  for k in range(n):
    ans += s[k]+pl[k]
  ans+=s[-1]
  total += eval(ans)
 
print(total)