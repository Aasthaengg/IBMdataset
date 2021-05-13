s = input()
dic = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
# -1のケース
if s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

# 出てきた文字をチェック
for c in s:
    dic[c] += 1

# 26文字未満の場合は最後に使っていない最小文字付け足す
if len(s) != 26:
    for k, v in dic.items():
        if v == 0:
            print(s + k)
            exit()
# 全種使っている
else:
    # どこからラストまで降順に並んでいるのか
    # ....stuvw zyx
    # ↑ならzyxが降順になっている
    left = 0
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            pass
        else:
            left = i + 1

    # 降順の部分を分離
    s_down = s[left:]
    check = s[left - 1]
    s_down = reversed(s_down)

    # s_down直前の文字より大きいかつs_down内の最小文字で直前の文字を置き換える
    # ....stuvw zyx
    # なら，wをzyxの中の最小かつwより大きいxで置き換え
    for c in s_down:
        if check < c:
            print(s[:left-1] + c)
            exit()
