s = input()
n = len(s)
l = [0 for i in range(n)]
cou = 0
for i in range(n):
  k = s[i]
  if k=="B":
    l[i] += 1+l[i-1]
  else:
    l[i] += l[i-1]
    cou += l[i]
#  print(l)
print(cou)