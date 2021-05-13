s = input()
no_x = s.replace('x','')

l = 0
r = len(s)-1
ans = 0
while l<r :
  if s[l] != s[r]:
    ans += 1
    if s[l] == 'x':
      l += 1
    else:
      r -= 1  
  else:
    l += 1
    r -= 1  

for i in range(len(no_x)//2):
  if no_x[i] != no_x[-i-1]:
    ans = -1

print(ans)    