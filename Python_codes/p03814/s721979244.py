s=input()

for i in range(len(s)):
  if s[i]=='A':break

for j in range(len(s)-1,-1,-1):
  if s[j] =='Z':break
    
print(j-i+1)