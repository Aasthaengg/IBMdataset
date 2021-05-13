N = int(input())
a_li = list(map(int, input().split()))
# 最初と最後を加えておく
total = abs(a_li[0]) + abs(a_li[-1])
for i in range(1, N):
    total += abs(a_li[i] - a_li[i - 1])
# 最初を取り除く
# 0, a[0], a[1]のうちa[0]が消えたら…
print(total - abs(a_li[0]) - abs(a_li[0] - a_li[1]) + abs(a_li[1]))
for i in range(1, N - 1):
    # a[i-1], a[i], a[i+1]のうちa[i]が消えたら…
    print(total - abs(a_li[i] - a_li[i - 1]) - abs(a_li[i + 1] - a_li[i]) + abs(a_li[i + 1] - a_li[i - 1]))
# 最後を取り除く
# a[-2], a[-1], 0のうちa[-1]が消えたら…
print(total - abs(a_li[-1]) - abs(a_li[-1] - a_li[-2]) + abs(a_li[-2]))
