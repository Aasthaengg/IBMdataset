n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

# A内での転置数
# N*N通り調べてもいいが、以下ではjはiによって絞られることを考慮した
x = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            x += 1

# y=Aの各要素について、それより小さい要素がA内にいくつ存在するか
# ex. [3,5,1]なら、3>1, 5>3, 5>1の3つ
y = 0
for a1 in a:
    for a2 in a:
        if a1 > a2:
            y += 1

# A内で発生する転倒数 * AはK個存在する
ans += x * k

# ...[3,5,1]...[3,5,1]...と2つのAを選ぶ時を考える
# このとき2つのA間での転倒は3つ、つまりyに等しくなる
# 2つのAの選び方はK_C_2
ans += y * k * (k - 1) // 2

ans %= 10**9 + 7
print(ans)
