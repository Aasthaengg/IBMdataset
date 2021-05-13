import sys
x,k,d = map(int,input().split())

# x:位置　k：回数　d:距離

#往復に辿りつく前に終わるパターン
if(abs(x)-d*k >= 0):
    print(abs(abs(x)-d*k))
#0またいで往復するパターン
else:
    #往復直前までにかかる回数
    r_count = abs(x)//d
 
    #残り捜査回数
    rest = k - r_count

    #残り回数の奇遇によって計算を判断
    #残り回数が偶数の時はr_count分動かした時と変わらない
    if(rest %2 == 0):
        print(abs(abs(x) - d*r_count))
    #残り回数が奇数:さらにD移動した分？
    else:
        print(abs(abs(abs(x) - d*r_count)-d))


#通らない.....



