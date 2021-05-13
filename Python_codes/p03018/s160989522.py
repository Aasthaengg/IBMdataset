s = input()
n = len(s)
d = [s[0]]
for i in range(1,n):
  if s[i]=="C" and s[i-1]=='B':
    d.pop()
    d.append("x")
  else:
    d.append(s[i])
q = "".join(d)
cou = 0
cou_a = 0
l = len(q)
for i in range(l):
  if q[i]=="A":
    cou_a += 1
  elif q[i]=="x":
    cou +=  cou_a
  else:
    cou_a = 0
print(cou)