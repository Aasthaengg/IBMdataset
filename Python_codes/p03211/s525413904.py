
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    s = input().rstrip()

    ans = 1000
    for i in range(len(s) - 2):
        num = int(s[i:i+3])
        if ans > abs(753 - num):
            ans = abs(753 - num)

    print(ans)



if __name__ == "__main__":
    resolve()
