import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B = map(int, readline().split())
    ans = (B-A)*(B-A+1)//2-B
    print(ans)



if __name__ == '__main__':
    main()
