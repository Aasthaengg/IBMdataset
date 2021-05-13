import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    K, T = map(int, readline().split())
    A = list(map(int, readline().split()))
    if sum(A)-max(A)+1 <max(A):
        print(max(A)*2-sum(A)-1)
    else:
        print(0)



if __name__ == '__main__':
    main()
