# input
N = int(input())

# check
if N < 4:
    print("No")
else:
    for seven_n in range(0, N + 1, 7):
        if (N - seven_n) % 4 == 0 or N - seven_n == 0:
            print("Yes")
            exit(0)
    print("No")