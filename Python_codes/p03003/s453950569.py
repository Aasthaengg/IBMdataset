import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N, M = map(int, readline().split())
    #空の部分列を考えるために適当な値で0番目の要素を埋めてインデックスを調節している
    #dpの更新で考えるのは1番目以降であるから0番目の要素が同じ要素であろうとなかろうと影響しない
    S = [0] + [int(i) for i in readline().split()]
    T = [0] + [int(i) for i in readline().split()]
    
    #共通部分列の集合と共通部分列の数対応について考えるために補助的にDPを定義
    #DP(i, j):=Sのi文字目、Tのj文字目までの共通部分列の集合

    #実際に求める数を導くためのdpテーブル
    #dp(i, j):=Sのi文字目、Tのj文字目までの共通部分列の数

    #「受け継ぐ要素（変化しない共通部分列）」と「増える分の要素」に注目して考える
    #S_i+1 != T_j+1のとき、DP(i+1, j+1) = DP(i+1, j) ∩ DP(i, j+1) 
    #S_i+1 = T_j+1のとき、DP(i+1, j+1) = DP(i+1, j) ∩ DP(i, j+1) ∩ (操作によって増えた共通部分列の集合)
    #（操作によって増えた共通部分列の集合）の要素数はdp(i, j)である
    # ∵ DP(i, j)の各要素である共通部分列の最後にそれぞれS_iを追加してできた共通部分列の集合が（操作によって増えた共通部分の集合）である

    #DPをdpに対応付けながら実装していく

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)] 

    #空の部分列が共通部分列となるので、dp[0][x]およびdp[x][0]の値は1として初期化する
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(M+1):
        dp[0][i] = 1
    
    #dpの更新
    P = int(1e9)+7
    for i in range(N):
        for j in range(M):
            if S[i+1] != T[j+1]:
                #和集合の要素数を考えるとき、重複部分の要素数を引かなければならない
                #DP(i+1, j)とDP(i, j+1)の重複部分はDP(i, j)であり要素数はdp(i, j)である
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j]
                dp[i+1][j+1] %= P
            else:
                #下の式の最後のdp[i][j]は増えた共通部分列の数である
                #dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + dp[i][j] 
                #整理すると以下の式になる
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] 
                dp[i+1][j+1] %= P
    print(dp[N][M])
if __name__ == '__main__':
    main()
