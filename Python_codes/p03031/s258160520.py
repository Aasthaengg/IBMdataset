def mod2(num):
    return num % 2

def solve():
    # 標準入力
    N, M = list(map(int, input().split()))  # N: スイッチの数， M: 電球の数
    k = [0] * M  # 電球iにつながっているスイッチの数
    s = [[0] for _ in range(M)]  # 電球iにつながっているスイッチの番号
    for i in range(M):
        tmp = list(map(int, input().split()))
        k[i] = tmp[0]
        s[i] = tmp[1::]
    p = list(map(int, input().split()))

    # スイッチの状態を総当たり
    count = 0
    for switch_state in range(2**N):
        p_tmp = [0] * M
        iter_num = format(switch_state, '0'+str(N)+'b')
        # 電球ごとに条件をチェック, i: i番目の電球，s_i: i番目の電球に接続しているスイッチのリスト
        for i, s_i in enumerate(s):
            # 電球iに接続しているスイッチs_i_jがon/offかチェック
            for s_i_j in s_i:
                if (iter_num[s_i_j-1] == '1'):
                    p_tmp[i] += 1
        if(p == list(map(mod2, p_tmp))):
            count += 1
    print(count)

if __name__ == "__main__":
    solve()