# 解法 おそらくアルゴリズムの授業で出た，単純に締め切りが近いものからやっていくのが正しいのではないかと思われる．
#
N = int(input())
AB = []
for _ in range(N):
    a,b = map(int,input().split())
    AB.append([a,b])

AB.sort(key=lambda x: x[1])

# 最速でタスクをクリアしつつ，もし最短時間でも締め切りを過ぎた場合はだめ．
now = 0
for ab in AB:
    a,b = ab
    now += a
    if now>b:
        print('No')
        exit()

print('Yes')

