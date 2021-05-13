#全体的な方針
#浅いほうから貪欲に頂点を倍化していく
#現在見ている段の頂点数がそれより深い段の葉の数を超えると余ってしまう
#よって、minで押さえつける必要がある(累積和で高速化が必要)


#累積和の定義
def Csum(a):
    b,c=[],0
    for i in range(len(a)):
        c+=a[i]
        b.append(c)
    return b

#n:二分木の深さ
#a:それぞれの段数の葉の数
#s:aの累積和をとったもの(その深さよりも浅い葉の数)
#su:aの総和(全体の葉の数)
#b:現在の深さの頂点数
#c:現在までの頂点数

n=int(input())
a=list(map(int,input().split()))
s,su,b,c=Csum(a),sum(a),1,0
for i in range(n+1):
    #頂点数カウントに現在の段を加算
    #葉の数だけ親の候補を減らしておく
    c+=b
    b-=a[i]
    #最後まで頂点を使い切ったならcを出力
    #途中で頂点が足りなくなったら-1を出力
    if b<=0:
        if i==n and b==0:
            print(c)
        else:
            print(-1)
        break
    #次の段の頂点数の更新
    #iより深い葉の数(su-s[i])を超えないようにする
    b=min(b*2,su-s[i])