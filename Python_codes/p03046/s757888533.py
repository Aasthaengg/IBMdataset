m, k = [int(item) for item in input().split()]

if m == 0:
    if k == 0:
        print("0 0")
    else:
        print(-1)
        exit()
elif m == 1:
    if k == 0:
        print("0 0 1 1")
    else:
        print(-1)
        exit()
else:
    if k >= 2**m:
        print(-1)
        exit()
    for i in range(2**m):
        if i == k:
            continue
        print(i, end=" ")
    print(k, end=" ")
    for i in range(2**m-1, -1, -1):
        if i == k:
            continue
        print(i, end=" ")
    print(k)