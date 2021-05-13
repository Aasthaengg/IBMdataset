x = input()
w, h, x, y, r = [int(x) for x in x.split()]
if x - r >= 0 and x + r <= w:
    if y - r >= 0 and y + r <= h:
        print('Yes')
    else:
        print('No')
else:
    print('No')