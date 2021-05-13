s = input()

l = []
for i in range (len(s)):
    if (i+1) % 2 == 1:
        l.append(s[i])
        
print("".join(l))