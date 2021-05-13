def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    x = a[0]
    for v in a:
        if v % x == 0:
            continue
        x = v % x
    f = False
    for v in a:
        if k <= v and (v-k)%x == 0:
            f = True
    if f:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()