n = int(input())
h = list(map(int, input().split()))

# 右側に2以上小さい数字があったらダメ
minh = 10**9
for i in reversed(h):
    if i >= minh + 2:
        print('No')
        exit()
    minh = min(minh, i)
print('Yes')    