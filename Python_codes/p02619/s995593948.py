# d日目の終わりの低下する満足度
def cost(c, d, lastdi):
    total = 0
    # print("{}日目".format(d))
    # print(lastdi)
    for i in range(26):
        total += c[i]*(d - lastdi[i])
    # print("cost:{}".format(total))
    return total

# 最終日
D = int(input())
# type毎の満足度の下がりやすさ
c = list(map(int, input().split()))
# [d,i]の満足度
s = [[] for _ in range(D)]
for d in range(D):
    si = list(map(int, input().split()))
    s[d] = si

# type毎の最後に開催された日を管理
lastdi = [0 for _ in range(26)]

ans = 0
for d in range(D):
    # d日目に選択されたtype
    typei = int(input()) - 1
    lastdi[typei] = d+1 # 日付なので+1
    ans += s[d][typei] - cost(c, d+1, lastdi)
    print(ans)

