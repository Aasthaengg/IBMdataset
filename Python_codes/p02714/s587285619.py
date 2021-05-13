n = int(input())
s = list(input())
ans = s.count('R')*s.count('G')*s.count('B')

for i in range(n):
  if s[i] == 'R':
    s[i] = 1
  elif s[i] == 'G':
    s[i] = 2
  elif s[i] == 'B':
    s[i] = 4
  
for i in range(n):
  for j in range(i+1, n):
    k = 2*j - i
    if k >= n:
      continue
    if s[i]+s[j]+s[k]==7:
      ans-=1

print(ans)
