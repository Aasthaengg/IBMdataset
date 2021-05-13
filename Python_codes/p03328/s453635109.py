# https://atcoder.jp/contests/abc099/tasks/abc099_b

a, b = map(int, input().split())

num = 0
for i in range(1, 999):
    if b - a == i + 1:
        num = i
        break
ans = num * (num + 1) // 2 - a
print(ans)