
def resolve():
    import sys
    import string
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n, m = [int(x) for x in input().rstrip().split(" ")]
    left = 1
    right = n
    for i in range(m):
        l, r = [int(x) for x in input().rstrip().split(" ")]
        if left < l:
            left = l
        if right > r:
            right = r

        if right < left:
            print(0)
            return

    print(right - left + 1)


if __name__ == "__main__":
    resolve()
