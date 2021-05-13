import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    ans = INF
    for a in range(1,N//2+1):
        b = N-a
        res = 0
        for i in str(a):
            res += int(i)
        for i in str(b):
            res += int(i)
        ans = min(ans, res)
    print(ans)




if __name__ == '__main__':
    main()
