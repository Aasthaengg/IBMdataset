import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, H = map(int, readline().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, readline().split())
        A.append(a)
        B.append(b)
    B.sort(reverse=True)
    B.append(0)
    A_max = max(A)
    ans = 0
    for b in B:
        if b<A_max:
            ans += math.ceil(H/A_max)
            print(ans)
            break
        else:
            H -= b
            ans += 1
            if H<=0:
                print(ans)
                break

if __name__ == '__main__':
    main()
