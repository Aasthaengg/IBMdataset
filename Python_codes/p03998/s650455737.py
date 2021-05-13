# B - 3人でカードゲームイージー
def main():
    sa = list(input())
    sb = list(input())
    sc = list(input())
    t = sa.pop(0)

    for _ in range(301):
        if t == 'a':
            if len(sa) == 0:
                print('A')
                break
            t = sa.pop(0)
        elif t == 'b':
            if len(sb) == 0:
                print('B')
                break
            t = sb.pop(0)
        elif t == 'c':
            if len(sc) == 0:
                print('C')
                break
            t = sc.pop(0)


if __name__ ==  "__main__":
    main()