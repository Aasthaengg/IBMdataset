N = int(input())
a = list(map(int, input().split()))

a_set = set(a)

if len(a_set) > 3:
    print("No")
elif len(a_set) == 3:
    x, y, z = a_set
    if a.count(x) == a.count(y) == a.count(z):
        if x ^ y ^ z == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
elif len(a_set) == 2:
    x, y = sorted(a_set)
    if x == 0:
        if a.count(x) * 3 == N:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    if sum(a_set) == 0:
        print("Yes")
    else:
        print("No")
