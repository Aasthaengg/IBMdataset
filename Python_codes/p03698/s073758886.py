
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    s = input().rstrip()
    chars = set()
    for c in s:
        if c in chars:
            print("no")
            return
        else:
            chars.add(c)

    print("yes")




if __name__ == "__main__":
    resolve()
