n, y = map(int, input().split())

if y % 1000 != 0:
    print('-1 -1 -1')
else:
    y //= 1000
    for man in range((y - n)//9 + 1):
        if (y - n - 9 * man) % 4 == 0:
            go = (y - n - 9 * man) // 4
            if (n - man - go) >= 0:
                print(man, go, n - man - go)
                break
    else:
        print('-1 -1 -1')            