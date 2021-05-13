s = input()

A = 0
Z = 0

for n in range(len(s)):
  if s[n] == "A":
    A = n
    break

for n in range(len(s)-1,-1,-1):
  if s[n] == "Z":
    Z = n
    break
print(Z-A+1)