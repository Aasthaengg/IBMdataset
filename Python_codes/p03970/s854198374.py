a = input()
b = "CODEFESTIVAL2016"
c = 0
for i in range(len(b)):
    if a[i] == b[i]:
        continue
    else:
        c = c + 1
print(c)