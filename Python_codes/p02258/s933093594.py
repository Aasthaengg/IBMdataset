def main():
    n = int(input())
    t0 = int(input())
    t1 = int(input())
    tmpmin = t0
    tmpmax = t1 - t0
    tmpmin = min(t0, t1)

    for _ in range(2,n):
        t = int(input())
        if t - tmpmin > tmpmax:
            tmpmax = t - tmpmin 
        if t < tmpmin:
            tmpmin = t
    print(tmpmax)


if __name__ == '__main__':
    main()

