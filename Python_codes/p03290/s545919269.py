d, g = map(int, input().split())
pc = [tuple(map(int, input().split())) for i in range(d)]

ans = float('inf')

for i in range(2**d):
    sum = 0
    cnt = 0
    nokori = set(range(1, d+1))
    for j in range(d):
        bitchk = 2**j
        if i & bitchk:
            sum += pc[j][0]*100*(j+1) + pc[j][1]
            cnt += pc[j][0]
            nokori.discard(j+1)
    if sum < g:
        use = max(nokori)
        # -(-(g-sum)//(use*100))は切り上げ除算
        # pc[use-1][0]はその点数帯の問題数（解ける最大数）
        # -(-(g-sum)//(use*100))でgを超えるのに必要な問題数を出せる。
        # ex) 300点問題が4問残ってるとする。不足している点数(g-sum)が500点のとき
        # -(-500//300)で2問解く必要があることがわかる。
        n = min(pc[use-1][0], -(-(g-sum)//(use*100)))
        # n = (-(-(g-sum)//(use**100)))
        sum += n * use * 100
        cnt += n

    if sum >= g:
        ans = min(ans, cnt)

print(ans)
