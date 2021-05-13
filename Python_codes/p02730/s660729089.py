S = input()
count = 0
N = len(S)
a = int((N-1)/2 )
b = int((N +3)/2)
if S[:a] ==S[b-1:]:
  pass
else:
  count +=1
SS = S[b-1:]

SSS =list(SS)
for i in range(len(SSS)):
  if SSS[i] != SSS[-i-1]:
    
    count +=1
if count==0:
  print('Yes')

else:
  print('No')