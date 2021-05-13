import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    count = 0
    for _ in range(N):
        l, r = map(int, readline().split())
        count += r-l+1
    print(count)



if __name__ == '__main__':
    main()