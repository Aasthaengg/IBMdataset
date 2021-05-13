def main():
    n, c, k = map(int, input().split())
    t = [int(input()) for _ in range(n)]
    t.sort()
    ans = 0
    passengers = 0
    first = t[0]
    for tn in t:
        if tn > first + k or passengers == c:
            ans += 1
            passengers = 0
            first = tn
        passengers += 1

    print(ans + 1)


if __name__ == '__main__':
    main()
