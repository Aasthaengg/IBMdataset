s = list(input())
ans = 0
cnta = 0
flagb = 0
flabc= 0
for i in range(len(s)):
  if s[i]=="A":
    if flagb==0:
      cnta+=1
    else:
      cnta=1
      flagb=0
  if s[i]=="B":
    if flagb==0 and cnta:
      flagb=1
    else:
      flagb=0
      cnta=0
  if s[i]=="C":
    if flagb and cnta:
      ans+= cnta
      flagb=0
    else:
      cnta=0
      flagb=0
print(ans)
