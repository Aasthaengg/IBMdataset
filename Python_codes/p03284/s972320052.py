s = input()
n, k = s.split()


if int(n) % int(k) == 0:
    print(0)
else:
    print(1)