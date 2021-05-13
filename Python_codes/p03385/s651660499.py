s = input()
a = 0
b = 0
c = 0
for i in range(len(s)):
    if s[i] == 'a':
        a += 1
    elif s[i] == 'b':
        b += 1
    elif s[i] == 'c':
        c += 1
if a == 1 and b == 1 and c == 1:
    print("Yes")
else:
    print("No")