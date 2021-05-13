from collections import Counter

H, W = map(int, input().split())
cntr = Counter()
[cntr.update(Counter(input())) for _ in range(H)]

if H % 2 and W % 2:
    has_one = False
    twos = 0
    for v in cntr.values():
        if v % 2:
            if has_one:
                print("No")
                exit()
            else:
                has_one = True
                twos += 2 if v == 3 else 0
        else:
            twos += v % 4
    print("Yes") if twos // 2 <= H // 2 + W // 2 and has_one else print("No")
elif H % 2 or W % 2:
    if H % 2:
        H, W = W, H
    twos = 0
    for v in cntr.values():
        if v % 2:
            print("No")
            exit()
        else:
            twos += v % 4
    print("Yes") if twos <= H else print("No")
else:
    print("Yes") if all(v % 4 == 0 for v in cntr.values()) else print("No")
