from collections import Counter
n = int(input())
l = list(map(int, input().split()))
E = [i for i in l[::2]]
O = [i for i in l[1::2]]
e=Counter(E).most_common() #偶数番目の位置にある数の出現回数を最頻度順に並べる
o=Counter(O).most_common() #奇数番目の位置にある数の出現回数を最頻度順に並べる

if e[0][0] != o[0][0]: #偶数列の最頻値と奇数列の最頻値が異なる場合、それぞれを最頻値で置き換えるだけ
    print(n-e[0][1]-o[0][1])
else:
    if len(e)==1 or len(o)==1: #偶奇数列で最頻地が同じかつ片方が一種類の時、もう一方を全部置き換えるしかない
        print(n//2)
    else: #そうでない場合最頻値とsecond最頻値で置き換える
        a=n-e[1][1]-o[0][1]
        b=n-e[0][1]-o[1][1]
        print(min(a,b))