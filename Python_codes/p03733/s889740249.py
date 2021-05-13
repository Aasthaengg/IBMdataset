import sys
from math import pi

def solve():
    input = sys.stdin.readline
    N, T = map(int, input().split())
    S = [int(i) for i in input().split()]
    count = 0
    S.append(10 ** 20)
    for i in range(1, N+1):
        if S[i] > S[i-1] + T: count += T
        else: count += S[i] - S[i-1]
    print(count)

    return 0

if __name__ == "__main__":
    solve()