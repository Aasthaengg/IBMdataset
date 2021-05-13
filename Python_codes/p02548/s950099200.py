def solve():
    N = int(input())

    numDivs = [0] * (N+1)
    for div in range(1, N+1):
        for x in range(div, N+1, div):
            numDivs[x] += 1

    ans = 0
    for C in range(1, N+1):
        ans += numDivs[N-C]

    print(ans)


solve()
