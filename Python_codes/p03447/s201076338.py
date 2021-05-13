import sys

def solve():
    input = sys.stdin.readline
    X = int(input())
    A = int(input())
    B = int(input())
    moneyLeft = X
    moneyLeft -= A
    while moneyLeft - B >= 0:
        moneyLeft -= B

    print(moneyLeft)

    return 0

if __name__ == "__main__":
    solve()