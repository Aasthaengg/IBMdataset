W, H, x, y, r = map(int, raw_input().split())

if 0 <= x <= W and 0 <= y <= H:
    rect = [(0, 0), (0, H), (W, 0), (W, H)]
    for a, b in rect:
        if min(abs(a-x), abs(b-y)) < r:
            print "No"
            break
    else:
        print "Yes"
else:
    print "No"