
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    # s = input().rstrip()

    n = int(input().rstrip())

    if n == 1:
        print(1)
        return

    prev = 2
    ln = 1

    for i in range(2, n+1):
        tmp = prev + ln
        prev = ln
        ln = tmp

    print(ln)





if __name__ == "__main__":
    resolve()
