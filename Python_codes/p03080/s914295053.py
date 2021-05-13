n = int(input())
s = input()
lis_r = []
lis_b = []
for i in range(n):
  if s[i] == "R":
    lis_r.append(s[i])
  else:
    lis_b.append(s[i])

if len(lis_r) > len(lis_b):
  print("Yes")
else:
  print("No")