import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    ans = 0
    for i in range(N):
        if i==A[A[i]-1]-1:
            ans += 1
    print(ans//2)


if __name__ == '__main__':
    main()
