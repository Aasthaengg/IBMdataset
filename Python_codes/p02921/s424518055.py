S,T = open(0).read().split()
a = 0

if S[0]==T[0]:
  a+=1
if S[1]==T[1]:
  a+=1
if S[2]==T[2]:
  a+=1
  
print(a)