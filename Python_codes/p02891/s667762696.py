s = input()
k = int(input())
l = 1
ans = 0
c = []

for i in range(len(s)-1):
  if s[i] == s[i+1]:
    l += 1
  else:
    if c == []:
      c.append(l)
    ans += l//2
    l = 1
    
ans += l//2
if c == []:
  c.append(l)
ans *= k

if len(s) == l:
  ans = k*l//2
elif s[0] == s[-1] and l%2 == 1 and c[0]%2 == 1:
  ans += k-1
  
print(ans)