import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
INF = float('inf')


def main():
    N = int(readline())
    total = 0
    maximum = 0

    for _ in range(N):
        p = int(readline())
        total += p
        maximum = max(maximum,p)

    ans = total - maximum//2
    print(ans)
if __name__ == '__main__':
    main()
