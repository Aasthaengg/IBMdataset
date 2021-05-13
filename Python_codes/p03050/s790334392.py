# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d

n = int(input())

i = 1
ans = 0
while i <= n ** 0.5 + 1:
    if (n - i) % i == 0 and (n - i) // i > i:
        ans += (n - i) // i
    i += 1
print(ans)
