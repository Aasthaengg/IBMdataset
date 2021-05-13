from collections import Counter

H,W,*n = open(0).read().split()
H = int(H)
W = int(W)
c = Counter([])
for x in n:
    c += Counter(x)
if H % 2 == 0 and W % 2 == 0:
    for x in c.values():
        if x % 4 != 0:
            print('No')
            break
    else:
        print('Yes')
elif H % 2 == 1 and W % 2 == 1:
    center = 0
    cross = H + W - 1
    corner = (H*W) - cross
    corner_filled = 0
    cross_filled = 0
    for x in c.values():
        if x % 2 == 1:
            if center == 0:
                center = 1
                y = x - 1
            else:
                print('No')
                break
        else:
            y = x
        if y % 4 == 0:
            if corner_filled + x < corner:
                corner_filled += x
            elif corner_filled == corner:
                if cross_filled + x > cross:
                    print('No')
                    break
                else:
                    cross_filled += x
            else:
                cross_filled += corner_filled + x - corner
                corner_filled = corner
        else:
            temp = (x//4) * 4
            if corner_filled + temp < corner:
                corner_filled += temp
            elif corner_filled == corner:
                if cross_filled + temp > cross:
                    print('No')
                    break
                else:
                    cross_filled += temp
            else:
                cross_filled += corner_filled + temp - corner
                corner_filled = corner
            if cross_filled + 2 > cross:
                print('No')
                break
            else:
                cross_filled += 2
    else:
        print('Yes')
else:
    if H % 2 == 1:
        center = W
        sides = (H*W) - W
    else:
        center = H
        sides = (H*W) - H
    center_filled = 0
    sides_filled = 0
    for x in c.values():
        if x % 4 == 0:
            if sides_filled + x < sides:
                sides_filled += x
            elif sides_filled == sides:
                if center_filled + x > center:
                    print('No')
                    break
                else:
                    center_filled += x
            else:
                center_filled += sides_filled + x - sides
                sides_filled = sides
        elif x % 2 == 0:
            temp = (x//4) * 4
            if sides_filled + temp < sides:
                sides_filled += temp
            elif sides_filled == sides:
                if center_filled + temp > center:
                    print('No')
                    break
                else:
                    center_filled += temp
            else:
                center_filled += sides_filled + temp - sides
                sides_filled = sides
            if center_filled + 2 > center:
                print('No')
                break
            else:
                center_filled += 2
        else:
            print('No')
            break
    else:
        print('Yes')