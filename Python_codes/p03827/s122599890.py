
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n = int(input().rstrip())
    s = input().rstrip()

    x = 0
    max_x = 0
    for c in s:
        if c == "I":
            x+=1
            if x > max_x:
                max_x = x
        else:
            x -= 1


    print(max_x)




if __name__ == "__main__":
    resolve()
