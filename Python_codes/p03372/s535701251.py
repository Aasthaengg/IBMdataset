#95d　高速化・整理
N,C = map(int, input().split())

#左右の折り返し毎に計算すると　2**(N-1) で地球爆発する。折り返しは無駄なので1回のみにする。
#すると、折り返し点N通り、時計回り・反時計回り2通り、計2Nの計算でOKとなる

#入力を読み込みつつ、時計回りの移動のカロリーを計算
xv_list = [(0,0)]
total_cal_list_cw = [0] #時計回りに進んだ時のカロリーリスト
max_total_cal_list_cw = [0] #時計回りに進んだ時、i以下最大のカロリーリスト
max_total_cal_cw = 0

for i in range(1,N+1): #10**5
    x,v = map(int, input().split())
    xv_list.append((x,v))
    total_cal_cw = total_cal_list_cw[i-1] + v - x + xv_list[i-1][0]
    total_cal_list_cw.append(total_cal_cw)
    
    if max_total_cal_cw < total_cal_cw:
        max_total_cal_cw = total_cal_cw
        
    max_total_cal_list_cw.append(max_total_cal_cw)

#半時計回り移動のカロリーを計算
rev_xv_list = [(0,0)] + [(C - xv[0],xv[1]) for xv in xv_list[:-(N+1):-1]] #xv_kistを逆順に読み込み、xは原点から反時計回り時の距離にする
total_cal_list_acw = [0] #反時計回り時のカロリーリスト。以下同様。
max_total_cal_list_acw = [0]
max_total_cal_acw = 0

for i in range(1,N+1): #10**5
    x,v = rev_xv_list[i][0],rev_xv_list[i][1]
    total_cal_acw = total_cal_list_acw[i-1] + v - x + rev_xv_list[i-1][0]
    total_cal_list_acw.append(total_cal_acw)
    
    if max_total_cal_acw < total_cal_acw:
        max_total_cal_acw = total_cal_acw
    
    max_total_cal_list_acw.append(max_total_cal_acw)    

    
#準備ができたので、最大に摂取できるカロリーを求める。
ans = 0

for i in range(1,N+1): #10**5
    #a.先に時計回りをする場合
    #折り返さない場合
    if ans < total_cal_list_cw[i]:
        ans = total_cal_list_cw[i]
    #折り返す場合
    total_cal = total_cal_list_cw[i] - xv_list[i][0] #原点まで戻る
    if total_cal > 0:
        total_cal += max_total_cal_list_acw[N-i]
        if ans < total_cal:
            ans = total_cal
    
    #b.先に反時計回りをする場合
    #折り返さない場合
    if ans < total_cal_list_acw[i]:
        ans = total_cal_list_acw[i]
    #折り返す場合
    total_cal = total_cal_list_acw[i] - rev_xv_list[i][0] #原点まで戻る
    if total_cal > 0:
        total_cal += max_total_cal_list_cw[N-i]
        if ans < total_cal:
            ans = total_cal
        
print(ans)