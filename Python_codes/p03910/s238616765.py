N = int(input())

targ = N
while targ > 1:
    l = 0
    r = targ
    #
    while l < r:
        m = l + (r - l) // 2
        # print("#", targ, (l, r), m * (m - 1) // 2, targ - m)
        if m * (m - 1) // 2 >= targ - m:
            r = m
        else:
            l = m + 1
    #
    print(l)
    targ -= l

if targ > 0: print(targ)