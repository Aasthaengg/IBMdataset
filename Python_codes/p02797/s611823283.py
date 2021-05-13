# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c

n, k, s = [int(i) for i in input().split()]

ans = [s] * k
if s == 10**9:
    ans += [1] * (n - k)
else:
    ans += [s + 1] * (n - k)
print(" ".join([str(i) for i in ans]))
