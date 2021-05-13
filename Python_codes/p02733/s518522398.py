H, W, K = map(int, input().split())
S = list(input() for i in range(H))

sum = [[0] * (W+1) for i in range((H+1))]
for i in range(H):
    for j in range(W):
        sum[i+1][j+1] = sum[i][j+1] + sum[i+1][j] - sum[i][j] + (1 if S[i][j] == '1' else 0)

ans = H + W - 2

for ptn in range(1<<H-1): # 2^H - 1 通り
    cand = 0

    sep = [0] # 横方向の分割リスト、ここ天才
    for i in range(H-1):
        if((ptn >> i) & 1): # & を取ることで、上の桁を消せる
            sep.append(i+1)
            cand += 1
    sep.append(H)

    left = 0 # left は直前の分割
    for pos in range(W):
    	cur = [] # cur は今見てるホワイトチョコの個数のリスト

    	# 横方向に分割されている各部分について
    	for i in range(len(sep) - 1):
    		cur.append(sum[sep[i+1]][pos+1] - sum[sep[i+1]][left] - sum[sep[i]][pos+1] + sum[sep[i]][left])

    	if max(cur) > K:
    		if left == pos: # 縦に分割できない場合(一列しかない場合)
    			cand = H * W
    			break
    		else:
    			cand += 1
    			left = pos

    ans = min(ans, cand)

print(ans)
