x,n = map(int,input().split())
if n == 0:
    print(x)
else:
    plist = list(map(int,input().split()))
    answer = 0
    diff = 0
    while answer == 0:
        if (x - diff) not in plist:
            answer = x - diff
            break
        elif (x + diff) not in plist:
            answer = x + diff
            break
        diff += 1
    print(answer)