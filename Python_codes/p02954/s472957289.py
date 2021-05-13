def resolve():
    S = list(input())
    ans = [0 for _ in range(len(S))]
    rcnt, lcnt = 0, 0
    border = None
    for i in range(len(S)):
        #print("[{}], {}, {}".format(i, rcnt, lcnt))
        if i == 0:
            rcnt += 1
            continue

        # R -> L
        if S[i-1]=="R" and S[i] == "L":
            border = i
        # L -> R
        elif S[i-1]=="L" and S[i] == "R":
            ans[border-1] += rcnt//2 + lcnt//2
            ans[border] += rcnt//2 + lcnt//2
            if rcnt%2==1:
                ans[border-1] += 1
            if lcnt%2==1:
                ans[border] += 1
            rcnt, lcnt = 0, 0
            border = None
        
        if S[i] == "R":
            rcnt += 1
        else:
            lcnt += 1
    ans[border-1] += rcnt//2 + lcnt//2
    ans[border] += rcnt//2 + lcnt//2
    if rcnt%2==1:
        ans[border-1] += 1
    if lcnt%2==1:
        ans[border] += 1
    print(*ans)


if '__main__' == __name__:
    resolve()
