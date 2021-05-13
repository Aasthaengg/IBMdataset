s = input()
num_g = 1
num_p = 0
if s[0]=="g":
  score = 0
else:
  score = 1
for i in range(1,len(s)):
  a = s[i]
  if num_g==num_p+1:
    num_p += 1
    if a=="g":
      score += 1
  else:
    num_g += 1
    if a=="p":
      score -= 1
print(score)