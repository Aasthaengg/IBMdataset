n = int(input())
s = input()
a = s.count('.')
g = [a]
b=0
while b<n:
  if s[b] == '.':
    a-=1
  else:
    a+=1
  g.append(a)
  b+=1
print(min(g))