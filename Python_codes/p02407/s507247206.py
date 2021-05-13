n = int(input())
num = list(map(int, input().split()))

if n == 1:
    print(num[0])
else:
    counter = 0
    for i in (reversed(num)):
        if counter == 0:
            print(i, end="")
        elif counter == n-1:
            print(" {}".format(i))
        else:
            print(" {}".format(i), end="")
        counter += 1
