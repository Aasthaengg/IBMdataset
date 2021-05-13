def abc175_c_3():
    x, k, d = map(int, input().split())

    def solve(x, k, d):
        """
        https://atcoder.jp/contests/abc175/editorial/52
        """

        x = abs(x)

        straight = int(min(k, x / d))
        k -= straight
        x -= straight * d

        if k % 2 == 0:
            return x
        else:
            return abs(x - d)

    ans = solve(x, k, d)
    print(ans)

if __name__ == '__main__':
    abc175_c_3()