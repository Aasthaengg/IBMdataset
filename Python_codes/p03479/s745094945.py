# https://atcoder.jp/contests/abc083/tasks/arc088_a

X, Y = map(int, input().split())

res = 1
while X*2 <= Y:
    X *= 2
    res += 1

print(res)