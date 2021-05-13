
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    # s = input().rstrip()
    a, b, c, k = [int(x) for x in input().rstrip().split(" ")]

    if abs(a - b) > 10**18:
        print("Unfair")
        return

    if k % 2 == 0:
        print(a - b)
    else:
        print(b - a)

if __name__ == "__main__":
    resolve()
