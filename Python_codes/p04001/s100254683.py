from itertools import product

S=input()
ans=0
for i in list(product([False,True],repeat=len(S)-1)):
  b=0
  a=S[0]
  for j in range(len(S)-1):
    if i[j]==False:
      a+=S[j+1]
    else:
      b+=int(a)
      a=S[j+1]
  b+=int(a)
  ans+=b
print(ans)
