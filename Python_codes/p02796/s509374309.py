from pprint import pprint


n = int(input())

xl = [list(map(int,input().split())) for _ in range(n)]

#2次元配列リストのソートでは0番目の要素が比較されるとのこと。
#https://note.nkmk.me/python-list-2d-sort/
#xl.sort()

robot_area = []

for i in range(n):
    startpoint = xl[i][0] - xl[i][1]
    endpoint = xl[i][0] + xl[i][1]
    #この後のsortのことを考えて、endpointを0番目の要素とする。
    robot_area.append([endpoint,startpoint])

robot_area.sort()

counter = 0

#初期値は負の無限大とする。
before_point = -float('inf')

for j in range(n):
    #開始エリアが前回の終了エリアより大きければOK
    if robot_area[j][1] >= before_point:
        counter += 1
        before_point = robot_area[j][0]
    else:
        pass

print(counter)