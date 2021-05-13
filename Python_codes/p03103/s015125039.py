import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    drink = [[int(a) for a in input().split()] for _ in range(N)]
    drink.sort()
    price = 0
    for i in range(N):
        a, b = drink[i]
        if b <= M:
            price += a * b
            M -= b
        else:
            price += a * M
            break
    print(price)

    return  0

if __name__ == "__main__":
    solve()