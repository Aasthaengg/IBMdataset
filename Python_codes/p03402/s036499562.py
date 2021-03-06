from math import ceil


def solve(string):
    b, a = map(int, string.split())
    h = 2 * ceil(max((a - 1) / 25, (b - 1) / 25)) + 1
    a -= 1
    b -= 1
    ans = []
    ans.append("{} {}".format(h, 100))
    for i in range(h):
        if i % 2 == 0:
            ans.append("." * 50 + "#" * 50)
        else:
            if a > 0 and b > 0:
                ma = min(a, 25)
                mb = min(b, 25)
                ans.append("#." * ma + "##" * (25 - ma) + "#." * mb + "##" * (25 - mb))
                a -= ma
                b -= mb
            elif a == 0 and b > 0:
                mb = min(b, 25)
                ans.append("." * 50 + "#." * mb + "##" * (25 - mb))
                b -= mb
            elif a > 0 and b == 0:
                ma = min(a, 25)
                ans.append("#." * ma + "##" * (25 - ma) + "#" * 50)
                a -= ma
            """
            ma = min(a, 25)
            mb = min(b, 25)
            ans.append("#." * ma + "##" * (25 - ma) + "#." * mb + "##" * (25 - mb))
            a -= ma
            b -= mb
            a = max(a, 0)
            b = max(b, 0)
            """
    return "\n".join(ans)


if __name__ == '__main__':
    print(solve(input()))
