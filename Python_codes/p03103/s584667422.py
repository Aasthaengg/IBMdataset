from sys import stdin
input = stdin.buffer.readline

def main():
    n, m = map(int, input().split())
    ab = [(0, 0)] * n
    for i in range(n):
        ab[i] = tuple(map(int, input().split()))

    ab.sort(key=lambda x: x[0])

    ans = 0
    for a, b in ab:
        if b < m:
            ans += a * b
            m -= b
        else:
            ans += a * m
            print(ans)
            break

main()