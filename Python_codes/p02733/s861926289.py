H,W,K = map(int,input().split())
S = [[int(i) for i in input()] for _ in range(H)]
ans = float("inf")

# bit全探索
for i in range(2**(H-1)):
    start = [0]
    end = []
    for j in range(H-1):
        if i >> j & 1 == 1:
            j += 1
            start.append(j)
            end.append(j)
    end.append(H)
    L = len(end)
    # 横に割った回数
    divcnt = L-1
    # 横に割った区割りごとの白チョコの個数
    wcnt = [0]*L
    # 探索列の横に割った区割りごとの白チョコの個数
    tmp = [0]*L
    for w in range(W):
        # 探索列の直前で縦に割ったか
        flag = False
        for idx in range(L):
            cnt = 0
            for h in range(start[idx],end[idx]):
                cnt += S[h][w]
                if cnt > K: break
            else:
                tmp[idx] = cnt
                wcnt[idx] += cnt
                if wcnt[idx] > K: flag = True
                continue
            break
        else:
            if flag:
                # 縦に割ったらその列から数え直し
                wcnt = tmp[:]
                divcnt += 1
            continue
        break
    else:
        ans = min(ans,divcnt)

print(ans)
