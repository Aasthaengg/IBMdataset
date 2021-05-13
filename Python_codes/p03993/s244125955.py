# n = int(input())
# a = list(map(int, input().split()))
# ans = [[i] for i in range(1, n+1)]
# print(ans)
# for i in range(n):
#     print(ans[i], a[i])
#     ans[i].apeend(a[i])
#     ans[a[i]-1].append(i)
# print(ans)
# これなんでダメだったかわからん

n = int(input())
b = list(map(int, input().split()))

adlist = [[] for i in range(n)]  # 交流のあるやつ同士の隣接リスト
for i in range(n):  # 1から順に見ていく
    x = i+1
    y = b[i]
    adlist[x-1].append(y)
    adlist[y-1].append(x)
# print(adlist)
count = 0
for i in range(n):
    if adlist[i].count(b[i]) == 2:
        count += 1
print(count//2)