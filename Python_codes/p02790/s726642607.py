A = input("")
L = A.split(" ")
a_s = ""
a = int(L[0])
b = int(L[1])

if (a < b):
    for i in range(b):
        a_s += str(a)
else:
    for i in range(a):
        a_s += str(b)

print(a_s)