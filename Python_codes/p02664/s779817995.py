s = input()
a = []

for i in range(len(s)):
    if s[i] == "P":
        a.append("P")
    else:
        a.append("D")
        
print(*a,sep="")