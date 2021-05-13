#!/usr/bin/env python3
def main():
    def expected_val(limit):
        # return (1 + limit) / 2
        return sum(range(limit + 1)) / limit

    N, K = map(int, input().split())
    P = [int(x) for x in input().split()]

    lst = [0]
    res = 0
    for p in P:
        res += expected_val(p)
        lst.append(res)
    ans = 0
    for i in range(N - K + 1):
        res = lst[i + K] - lst[i]
        ans = res if res > ans else ans
    print(ans)


if __name__ == '__main__':
    main()
