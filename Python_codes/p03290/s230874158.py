d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]
ans = 1001
for i in range(1<<d): # 0から2^D -1までの全難易度についてそれを解くか解かないかの組み合わせ
    count, score, left = 0, 0, 0
    for j in range(d): # 100からD*100の難易度まで
        if (i >> j) & 1: # j*100の難易度の問題を解く場合(最後の桁が1かで判定)
            score += (j+1)*100*pc[j][0] + pc[j][1] # 全部の問題をといてボーナスポイントも得る
            count += pc[j][0] # 全部の問題解いた分をカウント
        else: left = j # 解かない場合は全て残りに回される
    for j in range(pc[left][0]): # 残っている時
        if score >= g: break
          
        score += (left+1)*100 # gを超えない範囲で1つずつ足され、カウントされる
        count += 1
    if score >= g: ans = min(ans, count) # gを越えるカウントの中でもっとも小さいものが答え
print(ans)