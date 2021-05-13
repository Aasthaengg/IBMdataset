s = list(input())

#不等号の向きを記録する
memo = ""

#不等号の連続した個数を記録する
cnt = 0

#1つ前に数えた不等号の連続した個数を記録する
before_cnt = 0

#出力する答え
ans = 0

#文字列Sの連続した不等号の向きを数える
for x in s:
    #初めはmemoが空白なので,memoに不等号の向きを記録
    if memo == "":
        memo = x
    
    #不等号の向きが同じ場合は、数を1カウントしてループに戻る
    if memo == x:
        cnt += 1
        
    #不等号の向きが異なる場合
    else:
        #ansに和を加算する
        ans += cnt * (cnt+1) // 2
        
        #不等号の向きの変化が処理が必要な場合
        if memo == ">":
            if before_cnt < cnt:
                ans -= before_cnt
            else:
                ans -= cnt

        before_cnt = cnt
        cnt = 1
        memo = x
else:
    ans += cnt * (cnt+1) // 2
    if before_cnt < cnt:
        if memo == ">":
            ans -= before_cnt
    else:
        if memo == ">":
            ans -= cnt
    before_cnt = cnt
    cnt = 0
 
print(ans)
