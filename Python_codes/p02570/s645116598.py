a = input().split()

D = int(a[0])
T = int(a[1])
S = int(a[-1])


if D/S <= T:
    print('Yes')
else:
    print("No")