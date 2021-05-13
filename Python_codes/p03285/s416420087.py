N = int(input())

lst = []

for i in range(26):
    for j in range(15):
        if i*4+j*7 > 100:
            break
        else:
            lst.append(i*4+j*7)


if N in lst:
    print("Yes")
else:
    print("No")
