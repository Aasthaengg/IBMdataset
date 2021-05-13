n = int(input())

for i in range(15):
    n = n - 7*i
    if n < 0:
        print("No")
        exit()
    elif n % 7 == 0 or n % 4 == 0:
        print("Yes")
        exit()