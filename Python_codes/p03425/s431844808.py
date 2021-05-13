n = int(input())
s = [input() for i in range(n)]
l = [0] * 5
for i in range(n):
  if s[i][0] == "M":
    l[0] += 1
  elif s[i][0] == "A":
    l[1] += 1
  elif s[i][0] == "R":
    l[2] += 1
  elif s[i][0] == "C":
    l[3] += 1
  elif s[i][0] == "H":
    l[4] += 1
ans = 0
for j in range(3):
  for k in range(j+1, 4):
    for i in range(k+1, 5):
      ans += l[j] * l[k] * l[i]
print(ans)