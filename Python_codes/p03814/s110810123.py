s = input()
 
posA = 0
posZ = 0
 
for i in range(len(s)):
  if s[i] == "A":
    posA = i
    break
for j in range(len(s)):
  if s[-j-1] == "Z":
    posZ = len(s) - 1 - j
    break
 
print(posZ - posA + 1)