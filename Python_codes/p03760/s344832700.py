o = input()
e = input()

p = ""
for i in range(len(o) + len(e)):
    if i % 2 == 0:
        p += o[i//2]
    else:
        p += e[i//2]
print(p)
