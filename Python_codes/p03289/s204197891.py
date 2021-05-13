S = str(input())
N = len(S)

alpha2num = lambda c: ord(c) - ord('a') + 1
#print(alpha2num("a"))
#print(alpha2num("Z"))
p = 0
s = 0
for i in range(N):
  if i == 0:
    if S[i] != "A":
      p = 1
  elif 2 <= i <= N - 2:
    if S[i] == "C":
      s += 1
    else:
      if alpha2num(S[i]) < 0:
        p = 1
  else:
    if alpha2num(S[i]) < 0:
      p = 1 
      

  
  
if (p == 0) and (s == 1):
  print("AC")
else:
  print("WA")
