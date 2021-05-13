import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,M,D = map(int,input().split())
answer = (M-1) * 2 * (N-D) / (N * N)
if D == 0:
    answer /= 2
print(answer)