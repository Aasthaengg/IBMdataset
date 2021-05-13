import itertools
s = input()
ans=0
for i in list(itertools.product([0,1], repeat=len(s)-1)):
  b = 0
  a = s[0]
  for j in range(len(s)-1):
    if i[j] == 0:
      a+=s[j+1]
    else:
      b+=int(a)
      a=s[j+1]
  b+=int(a)
  ans+=b
print(ans)