import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
int1 = lambda x: int(x) - 1

def main():
    n, k = map(int, input().split())
    ans = 0
    for b in range(k + 1, n + 1):
        ans += (b - k) * ((n + 1) // b) + max(0, (n + 1) % b - k)
    if k == 0:
        ans -= n
    print(ans)

main()
