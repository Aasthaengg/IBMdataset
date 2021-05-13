from collections import defaultdict
def main():
    S = input() + 'T'
    x, y = map(int, input().split())
    #データ加工
    moveX, moveY = [], []
    if S[0] == 'T': moveX.append(0)
    move ={0:moveX, 1:moveY}
    direct = 0
    step = 0
    for s in S:
        if s == 'T':
            if step > 0:
                move[direct].append(step)
                step = 0
            direct ^= 1 
        else:
            step += 1
    #判定
    if possible(x, moveX[1:], moveX[0]) and possible(y, moveY):
        print('Yes')
    else:
        print('No')


def possible(target, move, offset=0):
    l = len(move)
    dp = [defaultdict(lambda:False) for _ in range(l+1)]
    #初期化
    dp[0][0] = True
    for i,m in enumerate(move):
        for key in dp[i]:
            dp[i+1][key+m] = True
            dp[i+1][key-m] = True
    return dp[l][target-offset]


main()