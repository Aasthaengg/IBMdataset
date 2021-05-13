# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    d, n = [int(x) for x in input().rstrip().split(" ")]

    if n == 100:
        n = 101

    print(n * (100 ** d))


if __name__ == "__main__":
    resolve()
