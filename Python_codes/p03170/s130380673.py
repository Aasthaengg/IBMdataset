import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
a = list(map(int, input().split()))

#dp[i][j]は残りi個でjが勝つかどうか（j=0 or 1）
dp = [[-1, -1] for _ in range(K+1)]
dp[0] = [0, 0]

for i in range(1, K+1):
    for j in range(2):
        if dp[i][j] > -1:
            continue

        flag = 1
        for x in a:
            if i >= x:
                flag *= dp[i-x][1-j]
        if flag == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = 0
            
print("First" if dp[K][0] else "Second")