s = [int(input()) for _ in range(int(input()))]

if sum(s) % 10 != 0:
    print(sum(s))
else:
    s.sort()
    for x in s:
        if x % 10 != 0:
            print(sum(s) - x)
            break
    else:
        print(0)