def solve():
    N, A, B = [int(i) for i in input().split()]
    ans = 0
    for i in range(1, N + 1):
        s = sum([int(x) for x in str(i)])
        if A <= s <= B:
            ans += i
    print(ans)


if __name__ == "__main__":
    solve()