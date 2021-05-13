"""
・ビーカーの総重量がFを超えないように
・ビーカー内に砂糖の溶け残りが出ないように（水100gに対しEg溶ける）
・できるだけ濃度の高い砂糖水を作る
この砂糖水の全質量と砂糖の量を答える

操作は
・水を　100*A or 100*B 追加
・砂糖を　C or D 追加

愚直に考えると、
（１）砂糖水の集合がある。これから一つ取り出して、
（２）水（100A or 100B）、砂糖（C or D）のいずれかを加える。行える操作は全部試すので、4通りに分岐
（３）溶け残りやFを超えるなどした場合は除外する
（４）（３）の判定を通過した各砂糖水に対し、これまでに作った砂糖水より濃度が大きければ、答えとして更新する
（５）（４）で評価した砂糖水を（１）の集合に戻す
のように、ありえるパターンを全部試す。
CやDが小さいと間に合わないはず。重複ができたりするとしんどい。

容器の最大容量Fが <=3000と小さい。
なので、今回は先に作れる水の重量を全探索で作っておいて、それらに砂糖を入れられるだけ入れる、の方法でやると、
水の操作と砂糖の操作を独立に行えるので、計算量を減らせる。
砂糖も初めに全探索で、何gのができるか全部つくっておいて、水と全部の組み合わせを試して～みたいな感じにしてもいいかも。
ビーカーが3000までなので、最大でも3000*3000の組み合わせなので、間に合いそう
"""

from collections import deque


A,B,C,D,E,F = map(int, input().split())

waters = set()
for i in range(F // (100*A) + 1):
    for j in range((F - 100*A*i) // (100*B) + 1):
        if 100*A*i + 100*B*j > F:
            continue
        waters.add(100*A*i + 100*B*j)

sugars = set()
for i in range(F // C + 1):
    for j in range((F - C*i) // D + 1):
        if C*i + D*j > F:
            continue
        sugars.add(C*i + D*j)


waters = list(waters)
waters.sort()
sugars = list(sugars)
sugars.sort()

ans = [0.0, 100*A, 0]

for w in waters:
    if w == 0:
        continue
    for s in sugars:
        if w+s > F:
            break
        if s / (w+s+0.0) > E / (E + 100.0):
            break
        
        if s / (w+s) > ans[0]:
            ans = [s / (w+s+0.0), w+s, s]

print(ans[1], ans[2])
