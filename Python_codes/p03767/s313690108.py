# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())

    a_list = [int(x) for x in input().rstrip().split(" ")]
    a_list.sort()

    print(sum([a for i, a in enumerate(a_list[n:]) if i % 2 == 0]))


if __name__ == "__main__":
    resolve()
