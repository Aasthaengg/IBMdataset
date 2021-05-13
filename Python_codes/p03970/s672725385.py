s = str(input())
a = "CODEFESTIVAL2016"
b = 0
for i in range(len(s)):
    if s[i] != a[i]:
        b += 1
print(b)