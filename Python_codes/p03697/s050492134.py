import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    A, B = map(int, readline().split())
    if A+B>=10:
        print('error')
    else:
        print(A+B)

if __name__ == '__main__':
    main()