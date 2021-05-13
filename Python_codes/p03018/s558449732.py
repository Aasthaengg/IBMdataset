s = input().replace("BC", "D")
a = 0
c = 0
for i in s[::-1]:
    if i == "D":
        c += 1
    elif i == "A":
        a += c
    else:
        c = 0
print(a)