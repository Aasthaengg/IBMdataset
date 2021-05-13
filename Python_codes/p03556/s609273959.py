n = int(input())
for i in range(n, 0, -1):
    if int(i**0.5) == i**0.5:
        print(i)
        exit()