def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = max(a)
    r = 0
    chk = 10**9+1
    for x in a:
        if abs(x-l//2) < chk and x != l:
            r = x
            chk = abs(x-l//2)
    print(l, r)


if __name__ == "__main__":
    main()
