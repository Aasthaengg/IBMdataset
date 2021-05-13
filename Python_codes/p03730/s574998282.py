a, b, c  = map(int,input().split())









"""
Aの倍数の集合を考える
s1 = a*1
s2 = a*2
s3 = a*3
・・・



Bで割ってC余る数の集合を考える
k0 = C
k1 = C + B
k2 = C + 2B
k3 = C + 3B
・・・
k999 = c + 999B

k0からk999まで、1000個の整数がひとつもAの倍数でないとしたら、
「Aの倍数ではない」とはつまり
Aで割ると1余る or 
Aで割ると2余る or
Aで割ると3余る or 
・・・
Aで割ると(A-1)余る
つまりパターンとしては A-1 通りしかない

Aで割ったときの余りが
k0 ... 1
k1 ... 3
k2 ... 1






for で回せば,YESの判定はなんとなくできそうだが
NOの判定はどうやればいい？





"""


k = []
result = 'NO'

for i in range(a+1):
    ## Bで割ってC余る数の集合を作る

    k.append(c + b*i)

for i in range(a+1):
    p,q = divmod(k[i],a)   ## Aで割った商と余りを求める
    if q==0:
        result = 'YES'


print(result)




