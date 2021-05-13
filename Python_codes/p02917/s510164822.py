# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip())

    ans = 0

    prev = 0
    for i, b in enumerate(input().rstrip().split(" ")):
        b = int(b)
        if i == 0:
            ans += b
            prev = b
            continue

        ans += min(b, prev)
        prev = b
    ans += b

    print(ans)


if __name__ == "__main__":
    resolve()
