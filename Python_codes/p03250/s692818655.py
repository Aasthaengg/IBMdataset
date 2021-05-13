a = list(map(int, input().split(" ")))

a = sorted(a, reverse=True)

print(int(str(a[0]) + str(a[1])) + a[2])
