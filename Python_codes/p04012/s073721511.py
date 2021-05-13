w = input()

s = {}
for c in w:
    if c in s:
        s[c] += 1
    else:
        s[c] = 1
b = True
for k,v in s.items():
    b = b and v % 2 == 0

if b:
    print("Yes")
else:
    print("No")
