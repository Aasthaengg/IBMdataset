import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    X, A = map(int, readline().split())
    if X<A:
        print('0')
    else:
        print('10')

if __name__ == '__main__':
    main()