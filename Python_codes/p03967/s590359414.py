a = input()
b = ""
c = 0
for i in range(len(a)//2):
    b += "p"
for i in range(len(a) - len(b)):
    b += "g"
for i in range(len(a)):
    if a[i] == b[i]:
        c += 0
    elif a[i] == "g" and b[i] == "p":
        c += 1
    elif a[i] == "p" and b[i] == "g":
        c -= 1
print(c)
