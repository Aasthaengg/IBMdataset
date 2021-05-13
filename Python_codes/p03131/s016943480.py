K,A,B = map(int,input().split())
if K+1<=A:
    print(K+1)
else:
    if A+2>=B:
        print(K+1)
    else:
        #A+2枚→B枚
        #この状態になると叩くよりも交換した方が得
        #2回でB-A枚増えていく
        #奇数偶数で場合わけ
        if (K-A-1)%2==0:
            print(A+(B-A)*((K-A+1)//2))
        else:
            print(A+1+(B-A)*((K-A+1)//2))