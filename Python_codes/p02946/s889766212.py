# 問題：https://atcoder.jp/contests/abc137/tasks/abc137_b

k, x = map(int, input().strip().split())
res = [i for i in range(x - k + 1, x + k)]
res_str = ' '.join(map(str, res))
print(res_str)

