# ABC 104 C - All Green(my answer for bit)

D, G = map(int, input().split())
p, c = [], []
ans = float('inf')
for _ in range(D):
    a, b = map(int, input().split())
    p.append(a)
    c.append(b)

for bit in range(1 << D):  # bitで完答した問題を列挙
    score = 0
    cnt = 0
    comp = set(range(D))
    for i in range(D):  # 完答した問題のscoreを全て加算
        if bit & (1 << i):
            score += p[i] * 100 * (i + 1) + c[i]
            cnt += p[i]
            comp.discard(i)
    if score < G:  # scoreがGに満たなければ中途半端に解答する
        incomp = max(comp)
        # -が2つあるのは//で切り上げで計算するため．-がないと切り下げ
        # https://python.ms/division/#３つのやり方
        incomp_num = min(p[incomp],
                         -(-(G - score) // (100 * (incomp + 1))))  
        score += (incomp + 1) * incomp_num * 100
        cnt += incomp_num
    if score >= G:  # scoreが目標点G以上なら計算回数cntを記録
        ans = min(ans, cnt)
print(ans)