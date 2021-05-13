K, A, B = map(int, input().split())

if K == 1:
    print(2)
elif K == 2:
    if A == 1 and B >= 2:
        print(B)
    else:
        print(2)
else:
    ans = 1
    # 変換したほうが得なら変換する
    if B-A >= 2:
        # A枚を1円に変換、1円をB枚に変換で行動件を2回使うので2で割る
        cnt, amari = divmod(K-(A-1), 2)
        ans = A+cnt*(B-A)+amari
    else:
        ans += K
    print(ans)
