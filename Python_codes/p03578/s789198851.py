import sys
from collections import Counter
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7



def main():
    N = int(readline())
    D = list(map(int, readline().split()))
    M = int(readline())
    T = list(map(int, readline().split()))
    count_D = Counter(D)
    count_T = Counter(T)
    ans = 'YES'
    for key, value in count_T.items():
        if count_D[key]<value:
            ans = 'NO'
    print(ans)
if __name__ == '__main__':
    main()