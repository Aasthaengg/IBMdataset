N, K = map(int, input().split())
As = list(map(int, input().split()))


for i in range(K):
    #imos法(メモ)
    table = [0 for _ in range(N+1)]
    #数値がN個なのでN個の0の要素を作る
    #index0は空白、index1からx軸のランプがある位置に対応
    #1-Nまでのランプが格納されている
    for j in range(1,N+1):
        ai = As[j-1]
        #電球jが照らす左端をメモ
        #電球jが照らす左端はj-aiなので、ここに１を足す
        table[max(j-ai, 1)] += 1
        #電球jが照らす右端をメモ
        #電球jが照らす右端はj+aiなので、この次の項に-1を加える
        if j+ai<N:
            table[min(j+ai+1, N)] -= 1 

    #imos法(総和を求める)
    for j in range(1,N+1):
        table[j] += table[j-1]
        
    #答えになおす
    for j in range(N):
        As[j] = table[j+1]
        
    
    exit_condition = True
    for j in range(N):
        if As[j] != N:
            exit_condition = False
            break
        #要素が全てNの時に、conditionはtrueのまま
    
    if exit_condition:
        print(*As)
        exit(0)#条件が正常に動作した時、ここで終了とさせる
            

print(*As)

