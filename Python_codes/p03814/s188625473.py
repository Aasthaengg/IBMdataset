s = input()
minA = 200000
maxZ = 0
for i in range(len(s)):
    if s[i] == "A":
        if i < minA:
            minA = i
    elif s[i] == "Z":
        if maxZ < i:
            maxZ = i

print(maxZ - minA + 1)
