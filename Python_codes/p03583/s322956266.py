a = int(input())
for b in range(1,3501):
    for c in range(1,3501):
        if ((4*b*c)/a)-c-b == 0:
            continue
        k = b*c/(((4*b*c)/a)-c-b)
        if k <= 0:
            continue
        if k == int(k):
            print(b,c,int(k))
            exit()