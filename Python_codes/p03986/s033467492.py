s = input()
ans = len(s)
temp1 = 0 #Sが連続
for i in range(len(s)):
  if s[i] == "S":
    temp1+=1
  elif s[i] == "T":
    if temp1 > 0:
      temp1-=1
      ans-=2
    else:
      temp1=0
  else:
    temp1=0
print(ans)