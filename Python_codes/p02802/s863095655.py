# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n, m = [int(x) for x in input().rstrip().split(" ")]

    ac = [False for _ in range(n)]
    wa = [0 for _ in range(n)]
    wa_sum = 0

    for i in range(m):
        p, s = input().rstrip().split(" ")
        p = int(p) - 1
        if ac[p]:
            continue
        if s == "WA":
            wa[p] += 1
        else:
            ac[p] = True
            wa_sum += wa[p]
    print(len([x for x in ac if x]), wa_sum)


if __name__ == "__main__":
    resolve()
