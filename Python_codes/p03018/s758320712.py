# 実装する
# BCをXとしたとき、AとXだけが含まれる部分列は操作終了後に左側にX右側にAが詰まる
# AXXAAXのときはXXXAAAになる Aが右側に移動すると考える
# Aの移動距離 部分列長6にAが3個ある それぞれのAの初期位置から最終的に移動する位置までの距離
# （Aの初期位置位置[1 4 5]が最終的に[4 5 6]にくるのでその差）
# しゃくとりっぽい操作でいけそう
s = input()
t = s.replace("BC", "X", len(s))
ans = 0
left, right = 0, 0
while left < len(t):
    # 部分列の左端を見つける
    if t[left] not in ["A", "X"]:
        left += 1
        continue
    a_indicies = []
    a_count = 0
    a_idx = 0
    if t[left] == "A":
        a_indicies.append(a_idx)
        a_count += 1
    right = left + 1
    a_idx += 1
    while right < len(t) and t[right] in ["A", "X"]:
        if t[right] == "A":
            a_indicies.append(a_idx)
            a_count += 1
        right += 1
        a_idx += 1
    # leftからrightまでの部分列にAしか含まれていないorXしか含まれていない場合は考えない
    if right - left != a_count and a_count != 0:
        for i in range(a_count):
            ans += ((right - left) - (a_count - i)) - a_indicies[i]  # 適当
    left = right + 1
print(ans)