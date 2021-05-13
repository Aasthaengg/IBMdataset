import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, K = map(int, readline().split())
    V = list(map(int, readline().split()))
    max_value = 0
    for L in range(N+1):
        for R in range(N+1):
            if L+R>K:
                break
            if L+R>N:
                break
            get = V[:L]
            if R>0:
                get += V[-R:]
            get.sort()
            rest = K - (L+R)
            minus = sum((1 if x<0 else 0 for x in get))
            if minus>rest:
                value = sum(get[rest:])
            else:
                value = sum((x for x in get if x>0))
            if value>max_value:
                max_value=value
    print(max_value)

if __name__ == '__main__':
    main()