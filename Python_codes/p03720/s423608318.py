# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline
    n, m = [int(x) for x in input().rstrip().split(" ")]

    ans = [0 for _ in range(n)]

    for i in range(m):
        a, b = [int(x) for x in input().rstrip().split(" ")]
        ans[a-1] += 1
        ans[b-1] += 1

    print("\n".join([str(a) for a in ans]))


if __name__ == "__main__":
    resolve()
