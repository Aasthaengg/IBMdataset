a = [int(i) for i in input().split()]
a = sorted(a)
diff = (a[2] - a[0]) + (a[2] - a[1])
if diff % 2 == 0:
    print(diff // 2)
else:
    print(2 + diff // 2)