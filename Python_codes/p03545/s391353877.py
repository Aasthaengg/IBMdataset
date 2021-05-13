# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline

    a, b, c, d = [int(x) for x in input().rstrip()]

    for o1 in [True, False]:
        for o2 in [True, False]:
            for o3 in [True, False]:
                ans = a
                ans += b if o1 else -b
                ans += c if o2 else -c
                ans += d if o3 else -d

                if ans == 7:
                    s = str(a)
                    s += "+" if o1 else "-"
                    s += str(b)
                    s += "+" if o2 else "-"
                    s += str(c)
                    s += "+" if o3 else "-"
                    s += str(d)
                    s += "=7"

                    print(s)
                    return


if __name__ == "__main__":
    resolve()
