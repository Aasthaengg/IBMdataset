N = int(input())
# 0スタート0エンドなので付け加えておく
a_li = [0] + list(map(int, input().split())) + [0]
total = 0
for i in range(1, len(a_li)):
    total += abs(a_li[i] - a_li[i - 1])
for i in range(1, len(a_li) - 1):
    # a[i-1], a[i], a[i+1]のうちa[i]が消えたら…
    print(total - abs(a_li[i] - a_li[i - 1]) - abs(a_li[i + 1] - a_li[i]) + abs(a_li[i + 1] - a_li[i - 1]))
