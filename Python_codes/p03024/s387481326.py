a = input()
o = 0
x = 0
for i in range(len(a)):
    if a[i] == "o":
        o += 1
    else:
        x += 1
if o + 15-len(a) >= 8:
    print("YES")
else:
    print("NO")