#CF
s = input()
n = len(s)
c = 0
f = 0
for i in range(n):
    if s[i] == 'C' and c == 0:
        c = i+1
    if s[i] == 'F':
        f = i+1
if c != 0 and f != 0 and c < f:
    print("Yes")
else:
    print("No")