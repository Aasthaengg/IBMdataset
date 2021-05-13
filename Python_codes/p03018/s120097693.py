s = input()
s = s.replace("BC", "D")
result = 0
i = 0
while i < len(s)-1:
    if s[i]=="A":
        y = 1
        for j in range(i+1, len(s)):
            i += 1
            if s[j]=="A":
                y += 1
            elif s[j]=="D":
                result += y
            else:
                break
    else:
        i += 1
print(result)