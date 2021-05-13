import sys

def solve():
    input = sys.stdin.readline
    S = int(input())
    #|ac - bd| == S, a == 10 ** 9
    a = 10 ** 9
    c = (S - 1) // a + 1
    bd = a * c - S
    if bd == 0: b, d = 0, 0
    else:
        for i in range(1, bd):
            if i ** 2 > bd: break
            if bd % i == 0:
                b, d = i, bd // i
                break
    print(0, 0, a, b, d, c)

    return 0

if __name__ == "__main__":
    solve()