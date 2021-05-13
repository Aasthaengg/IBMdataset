s = str(input())
s2 = ""

for i in range(len(s)):
    if i % 2 == 0:
        s2 += s[i]

print(s2)
