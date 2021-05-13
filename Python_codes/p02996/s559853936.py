def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x: x[1], reverse=True)
    lim = float("inf")
    for p, q in a:
        if q < lim:
            lim = q
        lim -= p
    if 0 <= lim:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()