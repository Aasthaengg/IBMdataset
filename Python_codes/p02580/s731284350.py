H, W, M = map(int,input().split())
Bomb = []
for _ in range(M):
    hi, wi = map(lambda x: int(x) - 1, input().split())
    Bomb.append((hi, wi))

counterH = [0] * H
counterW = [0] * W

for (hi, wi) in Bomb:
    counterH[hi] += 1
    counterW[wi] += 1

# 最大のところを選ぶ
max_h = max(counterH)
max_w = max(counterW)

count = 0
for (hi, wi) in Bomb:
    if counterH[hi] == max_h and counterW[wi] == max_w:
        count += 1

# 共通部分を確認 (-1)
ans = max_h + max_w
if count == counterH.count(max_h) * counterW.count(max_w):
    ans -= 1
print(ans)
