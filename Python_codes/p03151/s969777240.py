n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
plus = []
sum = 0
num = 0
for i in range(n):
    diff = A[i] - B[i]
    if diff < 0:
        sum -= diff
        num += 1
    else:
        plus.append(diff)
# ここから まず、引いても全部正だったとき(負がない)つまりnum = 0の時は何もしなくていい
if num == 0:
    print(0)
    exit()
else:
    res = num
    # plusの大きい物順にする
    plus = sorted(plus,reverse=True)
    p = 0
    for i in range(len(plus)):
        p += plus[i]
        res += 1
        if p >= sum:
            break
    if p >= sum:
        print(res)
    else:
        print(-1)
