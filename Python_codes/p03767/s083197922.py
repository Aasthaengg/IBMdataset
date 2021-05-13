import sys
import time
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[2*i +1]
    print(ans)

if __name__ == '__main__':
    main()