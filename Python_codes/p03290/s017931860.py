def rec(i, g, count, rem):
    global ans
    if i == 0:
        # 総得点がGを超えていなければ、remの中の最高配点の問題を解く
        if g < G:
            # 解く問題
            use = max(rem)
            c = min(pc[use-1][0], -(-(G-g) // (use*100)))
            count += c
            g += use*100 * c
            
            
        if g >= G:
            ans = min(ans, count)
            
    else:
        # 全部解かない
        rec(i-1, g, count, rem)
        # 全部解く
        rem[i] = 0
        rec(i-1, g+i*100*pc[i-1][0]+pc[i-1][1], count+pc[i-1][0], rem)
        rem[i] = i

# 入力
D, G = map(int, input().split())
pc = [[int(i) for i in input().split()] for j in range(D)]
# 解いてない問題リスト
rem = [i for i in range(D+1)]
ans = float("inf")

rec(D, 0, 0, rem)

print(ans)