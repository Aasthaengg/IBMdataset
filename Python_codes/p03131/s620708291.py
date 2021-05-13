K,A,B = map(int,input().split())

# 最終的にビスケットに交換するのが必要
if (B-A < 2) :
    # ビスケットたたいてるほうがアド
    print(K+1)
elif (K < A - 1) :
    # たたいてる間に終わってしまう(換金操作は2行動必要)
    print(K+1)
else :
    # 最初はA枚になるまでビスケットをたたく
    K -= (A-1)
    biscuits = A

    action = K // 2
    # A枚払ってB枚獲得
    biscuits += (B-A) * action
    
    if (K % 2 == 1) :
        biscuits += 1
    
    print(biscuits)
