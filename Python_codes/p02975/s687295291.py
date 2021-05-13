import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    for i in range(N):
        if i==0:
            a = A[i]
        else:
            a = a^A[i]
    if a == 0:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()
