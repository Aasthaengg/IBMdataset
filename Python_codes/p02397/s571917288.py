while True:
    Num = map(int, raw_input().split())
    a = Num[0]
    b = Num[1]
    Max = max(a, b)
    Min = min(a, b)

    if a == 0 and b == 0:
        break
    else:
        print "%d %d" %(Min, Max)