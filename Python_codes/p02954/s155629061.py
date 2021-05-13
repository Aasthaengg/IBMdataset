S = input() + "R" #以下ではRでってったときに値更新してるから最後にR加える
l = len(S)
ans = [0 for s in range(1, l)]
flag = 0
rcnt = 0
lcnt = 0
rpos = 0
lpos = 0
for i in range(l):
    if S[i] == "R":
        if flag == 1:#文字列がLRとなってるとき、直前のRLについて答える
            if rcnt % 2 == 0: #Rの個数が偶数
                ans[rpos] += rcnt // 2
                ans[lpos] += rcnt // 2
            else:
                ans[rpos] += rcnt// 2 + 1
                ans[lpos] += rcnt // 2
            if lcnt % 2 == 0:
                ans[rpos] += lcnt // 2
                ans[lpos] += lcnt // 2
            else:
                ans[rpos] += lcnt // 2
                ans[lpos] += lcnt // 2 + 1
            rcnt = 0
            lcnt = 0
        flag = 0
        rcnt += 1 #Rの個数求める
        rpos = i #右端のRの位置を求める
    elif S[i] == "L":
        if flag == 0:
            lpos = i #左端のRの位置を求める
        lcnt += 1 #Lの個数を求める
        flag = 1
print(*ans)