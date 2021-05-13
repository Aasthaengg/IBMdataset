a = sorted(list(map(int, input().split())))
if a[0]%2 == 1 and a[1]%2 == 1 and a[2]%2 == 1:
    print(a[0]*a[1])
else:
    print(0)
