n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = [-1]*(n+1)  # 何回目にそれぞれの頂点に到達したか
tmp = []  # 頂点の移動経路
pos = 1  # 初期位置
cnt = 0  # 移動回数
while 1:
    if l[pos] != -1:  # ある頂点に2回到達したとき
        t = cnt-l[pos]  # ループの長さ
        if k < cnt:
            print(tmp[k])
        else:  # 経路の長さより大きいとき、2回到達した頂点を始点として、最終的にループのどの頂点に到達するかを求める
            print(tmp[l[pos]+(k-cnt) % t])
        break
    l[pos] = cnt
    cnt += 1
    tmp.append(pos)
    pos = arr[pos-1]
