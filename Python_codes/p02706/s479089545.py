# B - Homework
# https://atcoder.jp/contests/abc163/tasks/abc163_b

N, M = map(int, input().split())
A = list(map(int, input().split()))

result = N - sum(A)

if result >= 0:
    print(result)
else:
    print(-1)
