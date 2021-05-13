# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d

N = int(input())
A = list(map(int, input().split()))
total = 1000

for k in range(N - 1):
    if A[k] <= A[k + 1]:
        kabu = total // A[k]
        total -= kabu * A[k]
        total += kabu * A[k + 1]

print(total)