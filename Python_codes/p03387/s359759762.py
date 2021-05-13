def solve():
    L = [int(i) for i in input().split()]
    L.sort()
    a, b, c = L
    ans = 0
    while b < c:
        a += 1
        b += 1
        ans += 1
    while a < b:
        a += 2
        ans += 1
    print(ans if a == b else ans + 1)


if __name__ == "__main__":
    solve()
