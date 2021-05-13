# https://atcoder.jp/contests/abc083/tasks/arc088_a
X, Y = map(int, input().split())
s = X
count = 1
while s <= Y:
    s *= 2
    count += 1
print(count-1)
