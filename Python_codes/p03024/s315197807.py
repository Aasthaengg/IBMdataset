S = input()
num = 0
for i in range(len(S)):
  if S[i] == "x":
    num += 1
if num <= 7:
  print("YES")
else:
  print("NO")