# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline

    n, m = [int(x) for x in input().rstrip().split(" ")]

    ab = {}
    for _ in range(n):
        a, b = [int(x) for x in input().rstrip().split(" ")]
        if a not in ab:
            ab[a] = 0
        ab[a] += b

    a_list = sorted(ab.keys())
    ans = 0
    for a in a_list:
        if m <= ab[a]:
            ans += m * a
            break
        else:
            ans += ab[a] * a
            m -= ab[a]

    print(ans)



if __name__ == "__main__":
    resolve()
