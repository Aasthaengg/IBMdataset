import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    n = int(input().rstrip())
    max_count = 0
    ans = 1
    for i in range(1, n+1):
        num = i
        count = 0
        while(num % 2 == 0):
            count += 1
            num = int(num / 2)
        if count > max_count:
            max_count = count
            ans = i
        # print(i, count)
    print(ans)


if __name__ == "__main__":
    resolve()
