import collections

H, W, K = map(int, input().split())

S = [[sign for sign in input()] for i in range(H)]

ans = [[] for i in range(H)]
count = 0
flag = True
empty_cnt = 0

for i, row in enumerate(S):
    C = collections.Counter(row)
    str_cnt = C["#"]
    
    # 1列にイチゴがないときは直前の列と同じ分割にすればよいが……
    if str_cnt == 0:
        # 以前の列に数字が入っていないときは以後の列と同じにしたい
        if i == 0 or ans[i-1] == []:
            # 先頭から何列目までが保留になっているかカウント
            flag = False
            empty_cnt += 1
        else:
            ans[i] = ans[i-1]
            
    # 1列にイチゴがあるときはイチゴが来るたびにカットを入れる（イチゴの個数-1回）
    else:
        count += 1
        buf = 0
        for sign in row:
            ans[i].append(count)
            if sign == "#" and buf < str_cnt - 1:
                count += 1
                buf += 1
    
# 保留になっている先頭分を埋める
if not flag:
    for i in range(empty_cnt):
        ans[i] = ans[empty_cnt]
    flag = True

# 出力
for row in ans:
    print(*row)