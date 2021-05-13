S = input()
now = 0
for i in range(len(S)):
  if S[i] == "+":
    now += 1
  else:
    now -= 1
print(now)