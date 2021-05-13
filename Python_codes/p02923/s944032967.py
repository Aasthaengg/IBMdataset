
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    # s = input().rstrip()

    n = int(input().rstrip())

    ans = 0
    prev = 0
    count = 0
    for h in input().rstrip().split(" "):
        h = int(h)
        if h <= prev:
            count += 1
        else:
            if count > ans:
                ans = count
            count = 0
        prev = h
    if count > ans:
        ans = count

    print(ans)




if __name__ == "__main__":
    resolve()
