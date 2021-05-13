s = input()

S = 0
T = 0

for c in s:
  if c == 'S':
    S += 1
  else:
    if S > 0:
      S -= 1
    else:
      T += 1
      
print(S+T)