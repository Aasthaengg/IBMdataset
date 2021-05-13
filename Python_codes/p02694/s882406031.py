X=int(input())
def ans165(X:int):
    cash=100
    count=0
    while True:
        # cash=int(cash*1.01)
        cash+=cash//100#元本に１パーセントの利子をつけ小数点以下切り捨て
        count += 1#利子をつける回数だけcountを増やす
        if cash>=X:#cashがXの値以上になったらループ終了
            break
    return count
print(ans165(X))
