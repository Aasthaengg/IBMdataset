# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    s = input().rstrip()
    k = int(input().rstrip())

    for i in range(k):
        if s[i] != "1":
            print(s[i])
            return

    print(1)


if __name__ == "__main__":
    resolve()
