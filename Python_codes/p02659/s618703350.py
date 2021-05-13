def main():
    ab = [_x for _x in input().split()]
    n = ab[1]
    bb = (int(n[0])*100 + int(n[2])*10 + int(n[3]))
    aa = int(ab[0])
    if aa == 0:
        print(0)
        return
    if bb == 0:
        print(0)
        return
    result = str(aa*bb)

    if len(result) <= 2:
        print(0)
    else:
        print(str(result)[:-2])


main()
