S = input()
T = input()
a = "No"

for n in range(len(S)):
  if S[n:]+S[:n]==T:
    a = "Yes"

print(a)