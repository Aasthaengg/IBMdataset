from itertools import product
a = "KIH"
b = "B"
c = "R"
A = []
for x in product((0,1),repeat=4):
    z = ""
    if x[0]==1:
        z="A"+a
    else:
        z = a
    if x[1]==1:
        z += "A"+b
    else:
        z += b
    if x[2]==1:
        z += "A"+c
    else:
        z += c
    if x[3]==1:
        z += "A"
    A.append(z)
S = input().strip()
if S in A:
    print("YES")
else:
    print("NO")