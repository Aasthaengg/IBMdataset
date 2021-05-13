import sys
input = sys.stdin.readline
# int(input()) # 入力が1つ
n, t = map(int, input().split()) # 入力が複数
people = [int(i) for i in input().split()] # 配列で数字

ans = 0
pre = 0
for i in range(n):
    if pre >= people[i]:
        ans += t - (pre - people[i])
    else:
        ans += t
    pre = people[i] + t
print(ans)