"""
例2:
R R L L L L R L R R L L
0 3 3 0 0 0 1 1 0 2 2 0

入力が 10 ** 5 以下なので行けるところまで移動が行われる。
最終的には"RL"の部分で行ったり来たりすることになるので、
これらには必ずそれぞれ1人以上いる。
'RL'の左側の'R'と右側の'L'の個数によって、間の'RL'の人数が決まる。
10 ** 100 は偶数なので、'RL'すぐ左隣の'R'に位置していた人は、
最終的には'R'の'L'の部分に行く(偶数のやつは偶数に、奇数のやつは奇数に移動)。
"""
S = input()
ans = [0] * len(S)
cnt_even = 0
cnt_odd = 0
r_idx = 0
l_idx = 0
S += 'R'    # 'LR'で終わらせたいため
for i in range(1, len(S)):
    if S[i - 1] == 'R' and S[i] == 'L':
        # 'RL'発見。'R'数え上げ終わり
        l_idx = i   # l_idx決定
        cnt_even += 1
        cnt_odd += 1
    elif S[i - 1] == 'R' and S[i] == 'R':
        # 'R'数え上げ
        r_idx = i   # r_idx決定
        if (i - 1) % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1
    elif S[i - 1] == 'L' and S[i] == 'L':
        # 'L'数え上げ
        if i % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1
    else:
        # 'LR'発見。'L'数え上げ終わり
        ans[r_idx] += cnt_even if r_idx % 2 == 0 else cnt_odd
        ans[l_idx] += cnt_even if l_idx % 2 == 0 else cnt_odd

        # カウントリセット
        cnt_even = 0
        cnt_odd = 0

        r_idx = i   # r_idx決定
print(*ans)
