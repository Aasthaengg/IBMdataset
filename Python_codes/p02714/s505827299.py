n=int(input())
s=input()

r = 0
g = 0
b = 0
for i in s:
  if i == 'R':
    r += 1
  elif i == 'G':
    g += 1
  else:
    b += 1

all = r*g*b
ho = 0
for i in range(0,n):
  for j in range(i+1,n):
    if s[i] == s[j]:
      continue
    k = 2*j-i
    if k >= n:
      continue
    if s[i] == s[k] or s[j] == s[k]:
      continue
    ho += 1
print(all-ho)