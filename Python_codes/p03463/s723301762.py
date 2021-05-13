import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, A, B = map(int, readline().split())
    diff = abs(A-B)
    if diff%2==0:
        print('Alice')
    else:
        print('Borys')

if __name__ == '__main__':
    main()