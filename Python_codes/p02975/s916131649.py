n = int(input())
a = list(map(int, input().split()))
a.sort()
if not n % 3 == 0:
    if a[n - 1] == 0:
        print("Yes")
    else:
        print("No")
else:
    x, y, z = a.count(a[0]), a.count(a[n // 3]), a.count(a[2 * (n // 3)])
    if x == y == z == n // 3:
        if a[0] ^ a[n // 3] ^ a[2 * (n // 3)] == 0:
            print("Yes")
        else:
            print("No")
    elif a[0] == 0 and x == n // 3 and y == z == 2 * (n // 3):
        print("Yes")
    elif a[n - 1] == 0:
        print("Yes")
    else:
        print("No")