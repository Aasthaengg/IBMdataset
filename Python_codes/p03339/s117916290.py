'''
制約
2 ≤ N ≤ 3×10^5(300,000)

入力例 3
8
WWWWWEEE

出力例 3
3

考え方：
Eを0, Wを1と置くと、
0000000X11111111 と並ぶようにすればよい。
そのために、値を変える数が最小になるリーダーの位置を調べればよい

-> 左端のW(West), 右端のE(East)はほぼ必ず向きを変える必要がある。


A. 全パターン試す
ある地点より左のWの数 + 右のEの数　の合計が最小になるパターンを求める（文字一致でカウント）
-> TLE

B. 全パターン
str.count('W')でやる
-> TLE

C. 「累積和」(cumulative sum)というアルゴリズムを使わないと解けない問題。学習して、使う！


'''

# from collections import deque # キュー、スタックに利用

# sys.stdin.readline() # 標準入力の高速化に利用
import sys
input = sys.stdin.readline

is_debug = False


def main():
    '''メイン処理'''
    n = int(input())
    sss = input()

    s_list = list(sss)

    W_sums = [0] * n # 累積和を入れるリスト
    E_sums = [0] * n # 累積和を入れるリスト
    W_sum = 0 # 左端から数えて、向きを変える必要のあるWの数
    E_sum = 0 # 右端から数えて、向きを変える必要のあるWの数
    
    if is_debug:
        print(W_sums)
    
    for i in range(n):
        if s_list[i] == 'W':
            W_sum += 1
        W_sums[i] = W_sum
        if s_list[n-i] == 'E':
            E_sum += 1
        E_sums[(n-1)-i] = E_sum

    if is_debug:
        print(W_sums)
        print(E_sums)
    
    # W_sums, E_sumsを用いて、向きを変える人数が最小となる値を見つける
    min_cost = float('inf')
    for i in range(n):
        # Wを振り向かせる人数
        if i == 0:
            W_cost = 0
        else:
            W_cost = W_sums[i-1]
        # Eを振り向かせる人数
        if i == n-1:
            E_cost = 0
        else:
            E_cost = E_sums[(i-1)+1]

        if is_debug:
            print(i, W_cost, E_cost)

        cost = W_cost+E_cost
        if cost < min_cost:
            min_cost = cost
    
    print(min_cost)

if __name__ == "__main__":
    # ファイル実行時に、main()関数を実行
    main()

