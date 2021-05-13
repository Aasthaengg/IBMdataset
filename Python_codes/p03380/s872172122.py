import bisect

N = int(input())
A = list(map(int, input().split()))

A.sort()

# 組み合わせの片方は最大値
n = A[-1]

# もう片方はnの半分に近い値
# 二分探索で最も近い値を見つける
mid = bisect.bisect(A, n/2)

# 一つ手前の値とどちらが近いかチェックして、近い方を出力する
if abs(n/2-A[mid-1]) > abs(n/2-A[mid]):
    print(n, A[mid])
else:
    print(n, A[mid-1])
