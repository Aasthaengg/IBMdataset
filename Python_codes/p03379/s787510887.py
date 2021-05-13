N = int(input())
XS = list(map(int, input().split()))
mid_low = sorted(XS)[len(XS) // 2 - 1]
mid_high = sorted(XS)[len(XS) // 2]
for x in XS:
    if x <= mid_low:
        print(mid_high)
    else:
        print(mid_low)
