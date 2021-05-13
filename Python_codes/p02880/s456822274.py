N = int(input())
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in a:
    if N / x in a:
        print("Yes")
        exit()
print("No")
