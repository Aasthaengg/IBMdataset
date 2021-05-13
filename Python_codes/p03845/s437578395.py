import sys
input = sys.stdin.buffer.readline
N = int(input())
T = [0] + list(map(int, input().split()))
sum_T = sum(T)
M = int(input())
# print('sum_T', sum_T)
for _ in range(M):
    p, x = map(int, input().split())
    # print('p, x', p, x)
    t = sum_T - T[p] + x
    print(t)
