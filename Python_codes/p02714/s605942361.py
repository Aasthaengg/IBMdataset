N = int(input())
S = input()

Rr = 0
Gr = 0
Br = 0
Rl = 0
Gl = 0
Bl = 0

for i in range(1,N):
  if S[i] == "R":
    Rr += 1
  elif S[i] == "G":
    Gr += 1
  else:
    Br += 1

ans = 0
for i in range(N-1):
  if S[i] == "R":
    ans += Gl*Br
    ans += Bl*Gr
    Rl += 1
  elif S[i] == "G":
    ans += Rl*Br
    ans += Bl*Rr
    Gl += 1
  else:
    ans += Rl*Gr
    ans += Gl*Rr
    Bl += 1
    
  if S[i+1] == "R":
    Rr -= 1
  elif S[i+1] == "G":
    Gr -= 1
  else:
    Br -= 1
  
for i in range(1, N-1):
  for k in range(1, min(i, N-1-i)+1):
    if S[i] != S[i+k] and S[i] != S[i-k] and S[i+k] != S[i-k]:
      ans -= 1
  
print(ans)
  
  

  

