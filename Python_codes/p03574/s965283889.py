H, W = map(int, input().split())
S = [input() for _ in range(H)]

## 下準備(1)：　H*Wマスの周囲を0で囲む
S.insert(0, "0"*W)
S.append("0"*W)
S = ["0" + s + "0" for s in S]
S = [s.replace("#", "1") for s in S]

## 下準備(2): 8方向をforループで回すためのリストを作る
delta_H = [-1, -1, -1, 0, 0, 1, 1, 1]
delta_W = [-1, 0, 1, -1, 1, -1, 0, 1]


## 実行：　一文字ずつ見ていき、"."の場合、周囲8方向の数字を足し算する
S_new = [""]*H

for i in range(1, H+1):
    for j in range(1, W+1):
        if S[i][j] == ".":
            ans = 0
            
            for k in range(8):
                if S[i + delta_H[k]][j + delta_W[k]] != ".":
                    ans += int(S[i + delta_H[k]][j + delta_W[k]])
                    
            S_new[i-1] += str(ans)
            
        else:
            S_new[i-1] += "#"
            
print(*S_new, sep="\n")