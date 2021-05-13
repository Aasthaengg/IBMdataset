def main():
    w, h, n = map(int, input().split())
    minx = miny = 0

    for _ in range(n):
        x, y, a = map(int, input().split())

        if a == 1:
            minx = max(minx, x)
        elif a == 2:
            w = min(w, x)
        elif a == 3:
            miny = max(miny, y)
        else:
            h = min(h, y)
    else:
        print(max(w-minx, 0)*max(h-miny, 0))
        


if __name__ ==  "__main__":
    main()