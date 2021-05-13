import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    A, P = map(int, readline().split())
    print((3*A+P)//2)

if __name__ == '__main__':
    main()