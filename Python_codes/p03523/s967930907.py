S = input()
possible = False

def f(s, index):
  global possible

  if possible:
    return

  if index >= len(S):
    possible = True if s == "AKIHABARA" or s+"A" == "AKIHABARA" else False
    return
    
  f(s+"A"+S[index], index+1)
  f(s+S[index], index+1)

if len(S) >= 10:
  print('NO')
else:
  f("", 0)

  if(possible):
    print('YES')
  else:
    print('NO')