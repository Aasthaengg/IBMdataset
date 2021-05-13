n = int(input())
d = {}

while n > 0:
    n -= 1
    c,m = input().split()

    if c == "insert":
        d[m] = 0

    else:
        if m in d:
            print("yes")
        else:
            print("no")
