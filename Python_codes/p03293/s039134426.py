S = input()
T = input()
s = []
t = []
for i in range(len(S)):
  s.append(S[i])
  t.append(T[i])
flag = 0
if s == t:
  print("Yes")
  flag += 1
else:
  for i in range(len(s)):
    A = s[0]
    s.remove(A)
    s.append(A)
    if s == t:
      print("Yes")
      flag += 1
      break
if flag == 0:
  print("No")
