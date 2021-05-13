n, k = [int(i) for i in input().split()]
if k > (n - 1)*(n - 2) // 2:
    print(-1)
else:
    ed = []
    for i in range(1, n):
        ed.append(" ".join(map(str, [1, i + 1])))
    kk = (n - 1)*(n - 2)//2 - k
    if not kk:
        print(len(ed))
        print("\n".join(ed))
        exit()
    for i in range(1, n):
        for j in range(i+1, n):
            ed.append(" ".join(map(str, [i + 1, j + 1])))
            kk -= 1
            if not kk:
                print(len(ed))
                print("\n".join(ed))
                exit()
