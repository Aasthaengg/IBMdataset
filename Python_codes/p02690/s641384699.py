X = int(input())
for i in range(10**4):
    for j in range(10**4):
        x = i - 10**4//2
        y = j - 10**4//2
        if x**5 - y**5 == X:
            s = str(x) + " " + str(y)
            print(s)
            break
    else:
        continue
    break
