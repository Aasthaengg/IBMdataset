import collections

n = int(input())
v = list(map(int, input().split()))

v_odd = []
v_even = []

for i, v in enumerate(v):
    if i % 2:
        v_even.append(v)
    else:
        v_odd.append(v)

# Counterに入れて、valueの降順にソート
v_odd_c = collections.Counter(v_odd)
v_odd_c = sorted(v_odd_c.items(), key=lambda x: x[1], reverse=True)
v_even_c = collections.Counter(v_even)
v_even_c = sorted(v_even_c.items(), key=lambda x: x[1], reverse=True)

# counterに一つしかkeyがないと面倒なので0が0回出たことを明示的に示しておく
# 制約上、0はvとしてあり得ないので問題ない（必ず0は0回出る）
v_odd_c.append([0, 0])
v_even_c.append([0, 0])

# print(v_odd_c)
# print(v_even_c)

if n != 2:
    o1 = v_odd_c[0]
    o2 = v_odd_c[1]
    e1 = v_even_c[0]
    e2 = v_even_c[1]

    # 最頻値が異なる場合
    if o1[0] != e1[0]:
        ans = n - o1[1] - e1[1]
    # 最頻値が等しい場合
    elif o1[0] == e1[0]:
        # o1,e2を採用する場合
        temp1 = n - o1[1] - e2[1]
        #o2, e1を採用する場合
        temp2 = n - o2[1] - e1[1]
        ans = min(temp1, temp2)

elif n == 2:
    if v_odd_c[0][1] != v_even_c[0][1]:
        ans = 0
    else:
        ans = 1

print(ans)
