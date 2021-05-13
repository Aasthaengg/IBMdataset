def calc(n):
    return sum(ord(c) - ord('0') for c in str(n))

def solve():
    n = int(input())
    ans = 1 << 60
    for i in range(1, n):
        a = n - i
        ans = min(ans, calc(a) + calc(i))
    print(ans)


if __name__ == "__main__":
    solve()
