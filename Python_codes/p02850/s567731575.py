'''catupper
ポイントA.再帰DFSで全ての頂点をチェックし、辺の色を求める。上限に注意。
ポイントB.入力に注意。
頂点が連結しているということは、そこに辺があるということ。
辺は頂点を結ぶので、辺が連結している二つの頂点(a[i], b[i])で表現され、
まず、辺をedgeに格納する。
辺の色は辞書color_dictに格納している。
辺である(a[i], b[i])をキーとして使って、color_dict[(a[i], b[i])]で
その辺に対応する色の番号が分かるようにしている。
辞書のキーが配列になっているので、注意。
ポイントC.色を頂点の順番で辺毎に出力する。辺の数は頂点-1個。
for i in range(n-1):  
    print(color_dict[(a[i], b[i])])
疑問点：色が新しくなるのは分かるけど、
色が1から再び使えるようになる仕組みは下の通りで良いのか？
'''

import sys
sys.setrecursionlimit(1000000)#DFSは再帰の上限回数に注意

n = int(input())
edge = [[] for i in range(n)]
#どの頂点とどの頂点が繋がっているかを格納しておく配列
a = [0] * n#頂点aに繋がっている頂点bの番号を格納しておく配列
b = [0] * n

for i in range(n-1):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1#0-indexにする
    b[i] -= 1
    edge[a[i]].append(b[i])#無向グラフとして入力する
    edge[b[i]].append(a[i])#二重配列に注意

color_dict = {}#色を格納しておく辞書
k = 0#求める色の数

def dfs(x, last = -1, ban_color = -1):
#lastは、どこから来たか、逆走を防ぐ。使っちゃいけない色も引数
#最初は、どこからも来ないし、どの色もOK
    global k#グローバル変数、宣言を忘れない
    color = 1#次の頂点については、再び1からチェックする
    #但し、繋がっている前の頂点と結ばれている辺の色は使えない
    for to in edge[x]:
    #このfor文はある頂点から繋がる次の頂点への辺の色を次々と決めている
    #同じ頂点に繋がる辺は同じ色に出来ないので、次々、色を新しくする
    #配列edgeに格納されている次の頂点toを順番にチェック。
    #edgeに格納されている、いま見ている頂点から繋がっている
    #全ての頂点をチェックすれば、dfs1回分のfor文はオシマイ。
    #次の頂点についても、同様にfor文でチェックし、
    #次の頂点から繋がる全ての頂点をチェックすることになるが、
    #それは次の話。    
        if to == last:continue
        #来た頂点に戻ろうとしたら、何もしない(条件1)
        if color == ban_color:color += 1
        #いま見ている頂点へ来た辺に使っている色なら、
        #新しい色にする(条件2)
        color_dict[(x, to)] = color#DFSして、color_dictに値が入る
        #使う色をタプルで辞書color_dictに格納する(作業)
        #辺(x, to)をキーとして、値colorをバリューに入れる。
        dfs(to, x, color)
        #深さ優先探索なので深く探索できる限り次から次へと探索する。
        #イメージ的には一つ下の階層の頂点を探索する。
        #いま見ている頂点ではないので、混乱しないこと。
        #次の頂点toについてDFS。来たのはxから。前の頂点で使った色はダメ。
        color += 1#いま見ている頂点から繋がる他の頂点へ行く辺の色として
        #新しい色を用意しておく(注意)
    k = max(k, color-1)    #何色を使ったか、その最大値を記録しておく。
    #用意した新しい色(上記の注意)は、まだ使っていないのでcolor-1。

dfs(0)#最初の頂点を示す0をDFSに入れてスタート。
#辞書color_dictに辺キーと色バリューが格納される。

print(k)#必要となる色数を出力
for i in range(n-1):
#辺の色を1から、辺の総数である頂点番号-1まで出力
    print(color_dict[(a[i], b[i])])
    #辺と色を格納した辞書に対してキーである辺を指定すると、
    #辺に対応する色が出力される
'''  以下の場合分けは不要。制約で1≤ai<bi≤Nだからか？
無向グラフで、aiで一通り、全ての辺が出力されるから？
    if (a[i], b[i]) in color_dict:#辞書から答を出力
        print(color_dict[(a[i], b[i])])
    else:
        print(color_dict[(b[i], a[i])])
'''
