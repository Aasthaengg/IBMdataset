import sys

def solve():
    N = int(input())
    T, A = [int(i) for i in input().split()]
    H = [int(i) for i in input().split()]

    dif = sys.maxsize
    ans = -1
    for i in range(N):
        t = T - H[i] * 6 / 1000
        if abs(t - A) < dif:
            dif = abs(t - A)
            ans = i + 1
    print(ans)

if __name__ == "__main__":
    solve()