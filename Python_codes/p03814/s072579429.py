s =str(input())
for i in range(len(s)):
    if s[i]=='A':
        a=i
        break
for j in reversed(range(len(s))):
    if s[j]=='Z':
        b=j
        break
print(b-a+1)