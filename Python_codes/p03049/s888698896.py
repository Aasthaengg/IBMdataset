n = int(input())
s = [input() for _ in range(n)]
ab = 0
ba = 0
last_a = 0
first_b = 0
for i in range(n):
  if s[i][0] == "B" and s[i][-1] == "A":
    ba += 1
  elif s[i][-1] == "A":
    last_a += 1
  elif s[i][0] == "B":
    first_b += 1
  ab += s[i].count("AB")
if last_a == 0 and first_b == 0:
  print(ab+ba-1) if ba != 0 else print(ab)
else:
  print(ab+ba+min(last_a,first_b))