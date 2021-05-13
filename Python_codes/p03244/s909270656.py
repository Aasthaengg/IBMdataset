def resolve():
    import math
    from collections import Counter
    n = int(input())
    v = [int(i) for i in input().split()]
    c0 = Counter(v[0::2]).most_common(2)
    c1 = Counter(v[1::2]).most_common(2)
    l0 = math.ceil(n / 2)
    l1 = n // 2
    if c0[0][0] != c1[0][0]:
        print(l0 - c0[0][1] + l1 - c1[0][1])
    else:
        if len(c0) == 1 and len(c1) == 1:
            print(n // 2)
        else:
            if len(c0) == 2 and len(c1) == 2:
                print(min(l0 - c0[0][1] + l1 - c1[1][1],
                          l0 - c0[1][1] + l1 - c1[0][1]))
            elif len(c0) == 1:
                print(l1 - c1[1][1])
            else:
                print(l0 - c0[1][1])


resolve()
