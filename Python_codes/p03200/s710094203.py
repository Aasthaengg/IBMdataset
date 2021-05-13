s = list(input())
l = []
for i in range(len(s)):
    if s[i] == "W":
        l.append(i)
print(sum(l) - s.count("W")*(s.count("W")-1)//2)