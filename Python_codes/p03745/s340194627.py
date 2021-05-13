import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    last = A[0]
    direction = 0
    ans = 1
    for i in range(1,N):
        if direction == 0:
            if last< A[i]:
                direction = 1
            elif last>A[i]:
                direction = -1
            last = A[i]
            continue
        if direction == 1:
            if last<=A[i]:
                last = A[i]
                continue
            else:
                last = A[i]
                direction = 0
                ans += 1
                continue
        if direction == -1:
            if last >= A[i]:
                last = A[i]
                continue
            else:
                last = A[i]
                direction = 0
                ans += 1
                continue
    print(ans)

if __name__ == '__main__':
    main()