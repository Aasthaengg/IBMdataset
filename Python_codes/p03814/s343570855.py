s = str(input())
a = 0
b = 0
for i in range(len(s)+1):
    if s[i] == "A":
        a = i+1
        break
    else:
        pass
for i in reversed(range(len(s))):
    if s[i] == "Z":
        b = i+1
        break
    else:
        pass
print(b - a + 1)