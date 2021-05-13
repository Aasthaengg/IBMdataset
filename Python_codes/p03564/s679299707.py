import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    K = int(readline())
    a = 1
    for _ in range(N):
        a = min(a+K, a*2)
    print(a)



if __name__ == '__main__':
    main()