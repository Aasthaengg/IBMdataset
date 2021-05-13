# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline
    import functools
    import operator

    n = int(input().rstrip())

    ans = 1
    for i in range(1, n+1):
        ans *= i
        ans = ans % 1000000007

    print(ans)



if __name__ == "__main__":
    resolve()
