a = [int(s) for s in input().split()]
if a[1] > a[2]:
    print("0")
elif a[1] == a[2]:
    print("1")
elif a[0] == 1:
    print("0")
else:
    mini = a[2] + a[1] * (a[0] - 1)
    maxi = a[1] + a[2] * (a[0] - 1)
    print(int(maxi) - int(mini) + 1)