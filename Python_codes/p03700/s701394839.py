import sys
input = sys.stdin.readline

n,a,b= map(int, input().split())
h= [int(input()) for i in range(n)]


# めぐる式二部探索、mid=攻撃回数
l=-1
r=pow(10,10)
while r-l>1:
    # rは常にOK、lは常にNG。
    mid=l+(r-l)//2
    # 残りの攻撃回数を記録
    x=mid
    # なんらかの判定
    for i in range(n):
        # 爆風で倒せる敵はスルー
        if mid*b>=h[i]:
            continue
        else:
            # 爆風で削りきれないモンスターを爆弾で削る
            y=-(-(h[i]-(mid*b))//(a-b))
            x-=y
            if x<0:
                break
    if x>=0:
        r = mid  # 判定がOKのとき→範囲を左に狭める
    else:
        l=mid # 判定がNGのとき→範囲を右に狭める

print(r)
