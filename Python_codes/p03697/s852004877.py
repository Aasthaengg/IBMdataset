##### 解けた #####

A,B=list(map(int,input().split(" ")))
sumAB=(A+B)

if sumAB<10: # 合計が10未満の場合そのまま出力
    print(sumAB)
else: # 10以上の場合、"error"と出力
    print("error")