s = input()

z = []
for i in range(2**4):
    a = ""
    b =  format(i, "04b")
    if b[0] == "1":
        a += "A"
    a += "KIH"
    if b[1] == "1":
        a += "A"
    a += "B"
    if b[2] == "1":
        a += "A"
    a += "R"
    if b[3] == "1":
        a += "A"
    z.append(a)

if s in z:
    print("YES")
else:
    print("NO")