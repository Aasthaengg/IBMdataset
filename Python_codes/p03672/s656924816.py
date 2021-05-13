s = list(input())
s = s[::-1]

del s[:2]
l = len(s)

while any(s[i] != s[l//2 + i] for i in range(l//2)):
    del s[:2]
    l = len(s)

print(l)
