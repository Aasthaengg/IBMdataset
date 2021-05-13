arr = input().split()
arr = list(map(int,arr))
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]


if (abs(b - a) <= d and abs(c - b) <= d) or abs(a-c) <= d:
    print('Yes')
else:
    print('No')
