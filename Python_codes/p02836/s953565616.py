s=input()
ne=0

si=s[::-1]

for i in range(len(s)):
  if s[i] != si[i]:
    ne+=1


print(ne//2)