import sys
from operator import itemgetter
from itertools import accumulate
def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    C = list(accumulate(A))
    dp = [0] * N
    for i in range(N-1):
        if C[i] * 2 >= A[i+1]:
            dp[i+1] = dp[i] + 1
    print(dp[N-1]+1)

if __name__ == '__main__':
    main()