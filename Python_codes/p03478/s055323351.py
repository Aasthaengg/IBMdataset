# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n, a, b = [int(x) for x in input().rstrip().split(" ")]
    ans = 0
    for i in range(1, n+1):
        x = sum([int(c) for c in str(i)])
        if x >= a and x <= b:
            ans += i

    print(ans)


if __name__ == "__main__":
    resolve()
