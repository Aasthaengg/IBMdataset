s = input()
l = len(s)

i = 0
while s[i] != "A":
    i += 1

j = 1
while s[l-j] != "Z":
    j += 1

print(l-j-i+1)
