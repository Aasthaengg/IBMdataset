s = list(input())

a=0
z=0
for i in range(len(s)):
    if s[i]=='A':
        a=i
        break
        
s=s[::-1]
for i in range(len(s)):
    if s[i]=='Z':
        z=i
        break
    
print(len(s)-(a+z))