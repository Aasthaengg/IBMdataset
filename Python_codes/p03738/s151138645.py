
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    # s = input().rstrip()

    a = int(input().rstrip())
    b = int(input().rstrip())

    if a > b:
        print("GREATER")
    elif a < b:
        print("LESS")
    else:
        print("EQUAL")

if __name__ == "__main__":
    resolve()
