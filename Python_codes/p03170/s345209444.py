N,K = map(int,input().split())
a = list(map(int,input().split()))

dp = [False]*(K+1)

for i in range(1,K+1):
    #初期化
    judge = False
    #選択できる石を選ぶ
    for stone in a:
        #小さい石から選ぶのでこの時点で負け
        if i - stone < 0:
            break
        #ひとつでも勝てるパターンが見つかり次第break
        if dp[i-stone] == False:
            judge = True
            break
    dp[i] = judge
            
print('First' if dp[K] else 'Second')