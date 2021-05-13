x, y = list(map(int, input().split()))
group = 0

a = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

if a[x] == a[y]:
    print("Yes")
else:
    print("No")