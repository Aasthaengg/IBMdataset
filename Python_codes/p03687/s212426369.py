S = input()
N = len(S)

L = "abcdefghijklmnopqrstuvwxyz"

ans = 10**9
for s in L:
    X = S
    res = ""
    cnt = 0
    while(1):
        res = ""
        if X.count(s)==len(X):
            break
        for i in range(len(X)-1):
            if X[i]==s or X[i+1]==s:
                res += s
            else:
                res += X[i]
        X = res
        cnt += 1
    ans = min(ans,cnt)

print(ans)