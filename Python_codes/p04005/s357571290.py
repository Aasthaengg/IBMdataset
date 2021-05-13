
def resolve():
    import sys
    input = sys.stdin.readline

    a, b, c = [int(x) for x in input().rstrip().split(" ")]

    if (a * b * c) % 2 == 0:
        print(0)
        return

    a, b, c = sorted([a, b, c])

    print(a * b)



if __name__ == "__main__":
    resolve()
