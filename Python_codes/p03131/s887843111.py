K, A, B = map(int, input().split())

ans = 0
if A >= B:
    #ひたすらたたく
    ans = 1 + K
else:
    #1円で増えるビスケットの枚数が2枚以下なら、たたいたほうがいい
    if B - A <= 2:
        ans = 1 + K
    else:
        #まずA枚にする
        k = K - (A - 1)
        if k < 2:
            ans = 1 + K
        else:
            #A枚を1円にかえて、1円をB枚に変える
            k -= 2 
            ans = B
            #残った手順でひたすらA枚を1円に、1円をB枚にする
            ans += (k // 2) * (B - A)
            ans += k % 2
print(ans)