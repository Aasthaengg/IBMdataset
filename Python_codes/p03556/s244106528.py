n = int(input())
for i in reversed(range(1, n+1)):
    if i % (i**0.5) == 0:
        print(i)
        exit()