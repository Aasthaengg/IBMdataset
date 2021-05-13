s = input()
P = input()
e = s + s
x = len(P)
m = 0
count = 0
for i in range(len(s)):
    if P == e[m:x]:
        count += 1
    m += 1
    x += 1
if count >= 1:
    print("Yes")
else:
    print("No")