def main():
    N = int(input().strip())
    A = [int(_a) for _a in input().strip().split()]
    Q = int(input().strip())
    BCS = []
    for i in range(Q):
        BCS.append([int(_bc) for _bc in input().strip().split()])

    Amap = {}
    for a in A:
        if a not in Amap:
            Amap[a] = 0
        Amap[a] += 1

    total = 0
    for k,v in Amap.items():
        total += (k*v)

    for bc in BCS:
        b = bc[0]
        c = bc[1]
        if b in Amap:
            num = Amap[b]

            del Amap[b]
            if c not in Amap:
                Amap[c] = 0
            Amap[c] += num

            total = total + num*c - num*b

        print(total)

main()

