s = input()
c = 0
f = 0
for i in range(len(s)):
    if s[i] == 'C':
        c += 1
    elif s[i] == 'F' and c > 0:
        f += 1

if f > 0:
    print("Yes")
else:
    print("No")