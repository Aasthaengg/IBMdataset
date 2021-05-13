def slove():
    import sys
    input = sys.stdin.readline
    a = int(input().rstrip('\n'))
    b = int(input().rstrip('\n'))
    if a > b:
        print("GREATER")
    elif a < b:
        print("LESS")
    else:
        print("EQUAL")


if __name__ == '__main__':
    slove()
