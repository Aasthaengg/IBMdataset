import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import product
    s = input()
    c = ["KIH", "B", "R", ""]
    p = []

    for bit in product(range(2), repeat=4):
        cur = ""
        for i in range(4):
            if bit[i]:
                cur += "A"
            cur += c[i]
        p.append(cur)

    if s in p:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
