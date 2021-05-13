s = input()
n = len(s)
R = [0]*n
L = [0]*n

r = -1
l = -1
for i in range(n):
  if s[-1-i] == 'R':
    r += 1
    R[-1-i] = r
  else:
    r = -1
  
  if s[i] == 'L':
    l += 1
    L[i] = l
  else:
    l = -1
    
ans = [0]*n
for i in range(n):
  if s[i] == 'R':
    p = R[i]  
    if p % 2 == 1:
      p += 1
    ans[i+p] += 1
  else:
    p = L[i]  
    if p % 2 == 1:
      p += 1
    ans[i-p] += 1
    
print(*ans)    