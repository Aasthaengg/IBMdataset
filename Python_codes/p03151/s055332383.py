"""
準備度の余剰分を不足分に充てる。
なるべく余剰分が大きいものから割り振っていく。
"""
N = int(input())
A_LI = list(map(int, input().split()))
B_LI = list(map(int, input().split()))
shortage_list = []
surplus_list = []
for i in range(N):
    if A_LI[i] == B_LI[i]:
        # 余剰(不足)分0のやつがリストに入ることを避けたいのでこうしとく↓
        continue
    elif A_LI[i] < B_LI[i]:
        shortage_list.append(B_LI[i] - A_LI[i])
    else:
        surplus_list.append(A_LI[i] - B_LI[i])
shortage_list.sort(reverse=True)
surplus_list.sort(reverse=True)
if sum(shortage_list) > sum(surplus_list):
    print(-1)
else:
    if len(shortage_list) == 0:
        print(0)
        exit()
    shortage_idx = 0
    surplus_idx = 0
    shortage = shortage_list[0]
    surplus = surplus_list[0]
    surplus_change_cnt = 1
    while shortage_idx < len(shortage_list):
        tmp = min(shortage, surplus)
        shortage -= tmp
        surplus -= tmp
        # 0以下になったらおかわりする
        if shortage <= 0:
            shortage_idx += 1
            if shortage_idx == len(shortage_list):
                break
            shortage += shortage_list[shortage_idx]
        elif surplus <= 0:
            surplus_idx += 1
            if shortage_idx == len(shortage_list):
                break
            surplus += surplus_list[surplus_idx]
            surplus_change_cnt += 1
    print(len(shortage_list) + surplus_change_cnt)
