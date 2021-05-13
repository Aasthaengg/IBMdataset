
def resolve():
    import sys
    input = sys.stdin.readline

    a, b, c = [int(x) for x in input().rstrip().split(" ")]

    max_num = max([a, b, c]) if (sum([a, b, c]) + max([a, b, c])) % 2 == 0 else max([a, b, c]) + 1

    print(int((max_num * 3 - sum([a, b, c])) / 2))




if __name__ == "__main__":
    resolve()
