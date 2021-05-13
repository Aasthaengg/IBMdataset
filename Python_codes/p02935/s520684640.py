# 問題：https://atcoder.jp/contests/abc138/tasks/abc138_c

n = int(input())
v = list(map(int, input().strip().split()))
v.sort(reverse=True)
res = 0
for i in range(n-1):
    res += v[i] / (2**(i+1))
res += v[-1] / (2**(n-1))

print(res)
