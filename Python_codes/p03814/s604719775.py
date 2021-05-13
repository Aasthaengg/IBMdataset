s = list(input())

a_idx = 0
z_idx = len(s) - 1
for i in range(len(s)):
  if s[i] == "A":
    a_idx = i
    break

for i in range(len(s)):
  if s[len(s) -1 -i] == "Z":
    z_idx = len(s) -1 -i
    break  

print(z_idx - a_idx + 1)