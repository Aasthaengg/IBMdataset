# どうせ何を喰っても自分のポイントは入るので、
# 高橋くんは青木くんの得られるポイントの最大のやつを,青木くんは高橋くんのvice versa
# 同じポイントならその中でも自分が得られるものが多いほうがいい
# ↑ ぜーーーーーーーーーーーーーーーーーんぜんだめでした

# 解説みた ぜんぜんわからん 無理 

n = int(input())
arr = []
used = [False for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    arr.append([i, a, b])

lis = sorted(arr, key=lambda x: x[1] + x[2], reverse=True)
takp, aokp = 0, 0

c = 0

while c < n:
    if c % 2 == 0:
        # 高橋くんのターン
        takp += lis[c][1]
    else:
        # 青木くんのターン
        aokp += lis[c][2]
    c += 1
print(takp - aokp)
