n,k = map(int,input().split())
s = input()

if s[k-1] =='A':
  s2 = 'a'
elif s[k-1] =='B':
  s2 = 'b'
else:
  s2 = 'c'
  
if k == 1:
  print(s2+s[1:n])
elif k == n:
  print(s[:k-1]+s2)
else:
  print(s[:k-1]+s2+s[k:n])