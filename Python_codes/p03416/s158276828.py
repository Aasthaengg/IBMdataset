
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    # s = input().rstrip()
    a, b = [int(x) for x in input().rstrip().split(" ")]

    ans = 0
    for num in range(a, b+1):
        s = str(num)
        if(s[0] == s[4] and s[1] == s[3]):
            ans += 1
    print(ans)


if __name__ == "__main__":
    resolve()
