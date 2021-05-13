n = int(input())

for i in range(n):
    i += 1
    j = i
    if (j % 3 == 0):
        print("", i, end="")
    else:
        while(j):
            if (j % 10 == 3):
                print("", i, end="")
                break
            else:
                j = int(j / 10)
print("")