a = input()

t, c = int(a.split(" ")[0]), int(a.split(" ")[1])

if not c:
    print(t)
else:
    b = input()
    lst = [int(x) for x in b.split(" ")]

    for i in range(c+2):
        if t - i not in lst:
            print(t - i)
            break
        if t + i not in lst:
            print(t + i)
            break
