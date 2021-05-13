s = input()
g = 0
p = 0
ans = 0
for i in range(len(s)):
  if s[i]=="g":
    g+=1
  else:
    p+=1
dif = g-p
print(dif//2)