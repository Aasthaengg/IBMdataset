S = input()
T = S[::-1]

for n in range(len(S)):
  if S[n]=="A":
    a=n
    break

for m in range(len(T)):
  if T[m]=="Z":
    z=len(S)-m
    break
    
print(z-a)
