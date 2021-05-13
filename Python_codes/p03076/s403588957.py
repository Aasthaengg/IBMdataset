import math


def resolve():
    import sys
    import string
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    a = int(input().rstrip())
    b = int(input().rstrip())
    c = int(input().rstrip())
    d = int(input().rstrip())
    e = int(input().rstrip())

    max_loss = 0
    ans = 0
    for x in [a,b,c,d,e]:
        if max_loss < (10 - (x % 10)) % 10:
            max_loss = 10 - (x % 10)
        ans += math.ceil(x / 10.0) * 10

    ans -= max_loss
    print(ans)

if __name__ == "__main__":
    resolve()
