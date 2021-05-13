import sys
def input(): return sys.stdin.readline().strip()


def main():
    n, k = map(int, input().split())
    ans = 0
    if k != 0:
        for b in range(k, n + 1):
            q, r = n // b, n % b
            ans += (b - k) * q + max(0, r - k + 1)
    else:
        ans = n**2
    print(ans)

if __name__ == "__main__":
    main()
