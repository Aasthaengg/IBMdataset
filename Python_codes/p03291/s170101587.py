import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    S = input()
    L = len(S)
    """
    dpなんですか、そうですか。。。（眼中になかった）
    '?'を総当たりで埋めてから考えるのではなく、
    i文字目までの問題の解を考えるのがミソ。具体的には
        dp[i][""]    = (i文字目まで見たときにまだどの文字も選んでいない方法)
        dp[i]["A"]   = (i文字目まで見たときに"A  "の１文字まで選んでいる方法)
        dp[i]["AB"]  = (i文字目まで見たときに"AB "の２文字まで選んでいる方法)
        dp[i]["ABC"] = (i文字目まで見たときに"ABC"の３文字まで選んでいる方法)
    をキーとする遷移を考える。

    （注意）この遷移を例えば
        dp[i]["A"] = (i文字目まで見たときに"A"の１文字を選ぶ方法)
    のようにすると、それまでにどの文字を選んできたかの情報が抜け落ちるのでダメ。
    """
    dp = [1, 0, 0, 0]
    if S[0] == "A": dp = [1, 1, 0, 0]
    if S[0] == '?': dp = [3, 1, 0, 0]
    #print("S[0]={}, dp[0]={}".format(S[0], dp))
    for i in range(1, L):
        if S[i] == 'A':
            dp = [dp[0], dp[1] + dp[0], dp[2], dp[3]]
        elif S[i] == 'B':
            dp = [dp[0], dp[1], dp[2] + dp[1], dp[3]]
        elif S[i] == 'C':
            dp = [dp[0], dp[1], dp[2], dp[3] + dp[2]]
        else: 
            # ここがミソ！！！'?'には３通り入る余地があって、
            # この文字を選ばなくても今までの取り方はすべて３倍カウントになる！
            dp = [dp[0] * 3, dp[1] * 3 + dp[0], dp[2] * 3 + dp[1], dp[3] * 3 + dp[2]]
        dp = [dp[0] % mod, dp[1] % mod, dp[2] % mod, dp[3] % mod]
        #print("S[{}]={}, dp[{}]={}".format(i, S[i], i, dp))
    print(dp[3])


if __name__ == "__main__":
    main()