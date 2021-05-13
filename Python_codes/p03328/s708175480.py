import sys
input = sys.stdin.readline
# int(input()) # 入力が1つ
a, b = map(int, input().split()) # 入力が複数

n = 1
t = 0
for i in range(2, 1000):
    if (n - i) - a == n - b:
        t = n
        break
    n += i
ans = t - a
print(ans)