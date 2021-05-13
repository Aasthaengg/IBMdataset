N = int(input())
M = 10**9+7

memo = [{} for _ in range(N+1)] #dict

def ok(last4):
#last4 は 末尾４文字
    for i in range(4):
        t = list(last4)
        if  i >= 1:
            t[i-1],t[i] = t[i],t[i-1]   #入れ替えはこう書ける、覚える
        if "".join(t).count("AGC") >= 1:
            return False
    return True

def dfs(cur, last3):    #深さ優先探索
# cur   は 再帰回数 current?
#last3  は 末尾３文字
    if last3 in memo[cur]:  #memoにlast3が登録されていたら
        return memo[cur][last3] #dictはこれでvalueが出てくる
    if cur == N:    #求める回数再帰したら
        return 1    # ×1 して終了
    ret = 0 #Return(戻り値)の意味か
    for c in "ACGT":
        if ok(last3+c): #禁則事項を破ってないなら
            ret = (ret+dfs(cur+1, last3[1:]+c)) % M
    memo[cur][last3] = ret
    return ret

print(dfs(0,"TTT"))