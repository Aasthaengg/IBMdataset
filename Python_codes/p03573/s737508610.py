a = sorted(list(map(int, input().split())))
if a[1] == a[0]:
    print(a[2])
elif a[1] == a[2]:
    print(a[0])
