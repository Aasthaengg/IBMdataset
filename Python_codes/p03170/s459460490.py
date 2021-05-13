N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (10 ** 5 + 10)
for i in range(1, K+1):
    # dp[i-a]の中でどこか一つでもFalseになるdp[i]があればTrueを設定する
    # dp[i-a]がFalseということは、次の手番の相手を負かす取り方が存在するということになるので、この手番でa個取って相手の順番に回してしまえば勝ちが確定する
    # お互いが交互に数字を言っていって、最後に30を言ったほうの負け（最大+3）まで
    # みたいなゲームと同じ構造だと考えていい。上記のゲームで勝つには最後の数から逆算していけば、勝てる数字がわかるのと似ている
    dp[i] = not all(dp[i-a] if i-a >= 0 else True for a in A)

print("First" if dp[K] else "Second")

