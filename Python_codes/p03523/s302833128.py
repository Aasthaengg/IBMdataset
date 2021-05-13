S = input()

L = []

def rec(s) :
  L.append(s)
  
  for i in range(len(s)) :
    if s[i] == 'A' :
      rec(s[:i] + s[i+1:])

rec('AKIHABARA')

if S in L :
  print('YES')
else :
  print('NO')