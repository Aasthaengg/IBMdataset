import sys
from collections import deque
s = deque(map(str, input().rstrip()))

# 辞書の最後は-1
if "".join(s) == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    sys.exit()

# 使える文字リスト作成
s = [ord(x) for x in s]

# 26文字未満なら、未使用の１文字を追加して終わり
if len(s) < 26:
    can_use = set(range(97, 123)) - set(s)
    s = s + [min(can_use)]

# 26文字の時は例外処理を入れる
else:
    add = []
    s = s[::-1]
    prev = s[0]
    add.append(prev)

    # 末尾がzならzを消去し、1文字前をzにして終わり
    if prev == 122:
        s[1] = 122
        s = s[::-1][:-1]

    # そうでなければ、初めて増加する値が減少するタイミングまで見る
    # 減少するポイントで、その時点で使える中で最小の文字に差し替え
    else:
        for i in range(1, len(s)):
            if prev > s[i]:
                add = [x for x in add if x > s[i]]
                s[i] = (min(add))
                s = s[::-1][:-i]
                break
            prev = s[i]
            add.append(prev)

# 文字列に戻す処理
s = [chr(x) for x in s]

print("".join(s))