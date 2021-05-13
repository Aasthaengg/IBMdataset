N, T = [int(i) for i in input().split()]  # 数字はなるべく早い段階でint型にしておいた方がわかりやすい

all_pattern_list = []
# 次のようにするともっとシンプルにall_pattern_list = [[c1, t1], [c2, t2], ... , [cN, tN]] という2次元リストを作れる
for i in range(N):
    all_pattern_list.append([int(j) for j in input().split()])  # もしタプルにしたい場合はtuple([int(j) for j in input().split()])とすればOK

INF = 1001
ans = INF  # 解が見つからなかった場合を判定できるようにコストが取り得ない大きな値を初期値に設定しておく
# どうせ最悪全部見ることになるのでソートしなくてもOK
for c, t in all_pattern_list:  # アンパックを使うとわかりやすい変数名を使える
    if t <= T:
        ans = min(ans, c)  # 暫定最小コストより小さい場合は最小コストを更新

if ans == INF:
    print("TLE")
else:
    print(ans)