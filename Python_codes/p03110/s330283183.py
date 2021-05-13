j, b = 0, 0
for _ in range(int(input())):
    m, jb = input().split()
    if jb == "JPY":
        j += int(m)
    else:
        b += float(m)
print(j + 380000 * b)