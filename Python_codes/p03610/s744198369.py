s = input()
soutput = []
for i in range(0, len(s)):
    if i % 2 != 1:
        soutput.append(s[i])
        
print("".join(soutput))