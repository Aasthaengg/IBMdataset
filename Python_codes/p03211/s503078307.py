import sys
S=input()
t=1000
for x in range(len(S)-2):
  if t>abs(753-int(S[x]+S[x+1]+S[x+2])):
    t=abs(753-int(S[x]+S[x+1]+S[x+2]))
print(t)