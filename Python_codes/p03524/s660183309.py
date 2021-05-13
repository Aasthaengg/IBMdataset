s = input()
a = 0
b = 0
c = 0
for i in s:
    if i == "a":
        a += 1
    if i == "b":
        b += 1
    if i == "c":
        c += 1

if max(a,b,c)-min(a,b,c) <= 1:
    print("YES")
else:
    print("NO")
