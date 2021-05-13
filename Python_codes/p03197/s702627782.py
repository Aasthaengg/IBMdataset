n = int(input())
ans = 'second'
for _ in range(n):
    a = int(input())
    if a%2 != 0:
        ans = 'first'
print(ans)

# 状態としてありえるのは、E:全て偶数 or O:いずれか1つ以上が奇数
# 最終的にEを押し付けられたら負けと考える（すべて0）
# 現状態がOであるなら、奇数のものだけを食べて、状態Eを相手に返すことができる
# 現状態がEであるなら、1つ以上食べる必要があるので、Oが相手に返る
# ここから、初期状態がOならばfirst, Eならばsecondが答えとなる