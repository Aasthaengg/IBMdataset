# 問題：https://atcoder.jp/contests/abc140/tasks/abc140_a

n = int(input())
b = list(map(int, input().strip().split()))
res = b[0]
for i in range(1, n-1):
    res += min(b[i-1], b[i])
res += b[-1]
print(res)
