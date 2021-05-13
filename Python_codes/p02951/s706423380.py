# 1.値を正しく取得
a, b, c = (int(x) for x in input().split())

# 2.正しく処理
mizu = b + c
amari = mizu-a

if amari <= 0 :
    print(0)

else :
    print(amari)