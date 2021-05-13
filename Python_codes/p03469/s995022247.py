s = input()
res = []
for i in range(len(s)):
    if i == 3:
        res.append(8)
    
    else:
        res.append(s[i])
    
print("".join(map(str, res)))