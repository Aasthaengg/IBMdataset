def main():
    # import sys
    # readline = sys.stdin.readline
    # readlines = sys.stdin.readlines

    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    pos = X[0]
    cnt = 0
    for x in X:
        walk = (x - pos) * A
        tele = B
        if walk < tele:
            cnt += walk
        else:
            cnt += tele
        pos = x
    
    print(cnt)


if __name__ == "__main__":
    main()
