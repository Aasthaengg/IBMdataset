N,K = map(int,input().split())
L = list(map(int,input().split()))
L = sorted(L)

MOD=10**9+7

ans=1
if N==K:
    for a in L:
        ans*=a
        ans%=MOD

#全部ふで奇数個
elif all(l<0 for l in L) and K%2==1:
    #小さい方からKこ
    for l in L[-K:]:
        ans*=l
        ans%=MOD
else:#生徒ふが入り混じり
    absL = sorted(L,key=lambda x:-abs(x))

    ans_cand=[v for v in absL[:K]]
    remain=[v for v in absL[K:]]

    if len(list(filter(lambda x:x<0,ans_cand)))%2==0:
        for a in ans_cand:
            ans*=a
            ans%=MOD
    else:
        ans_cand_min_neg = None
        ans_cand_min_pos=None
        remain_cand_max_neg=None
        remain_cand_max_pos=None

        for a in ans_cand:
            if a<0:
                ans_cand_min_neg=a

        #できるだけ絶対値が大きいやつ
        for a in remain:
            if a>=0:
                remain_cand_max_pos=a
                break

        #正の数をans_candから一つ取り除いき、remain_candから負の数を一つ取ってくる

        for a in ans_cand:
            if a>0:
                ans_cand_min_pos=a
        for a in remain:
            if a<=0:
                remain_cand_max_neg=a
                break

        NG=None
        if not None in {ans_cand_min_pos,ans_cand_min_neg,remain_cand_max_neg,remain_cand_max_pos}:
            A = abs(ans_cand_min_pos*remain_cand_max_pos)
            B = abs(ans_cand_min_neg*remain_cand_max_neg)
            if A>=B:
                ans_cand.append(remain_cand_max_pos)
                NG=ans_cand_min_neg
            else:
                ans_cand.append(remain_cand_max_neg)
                NG=ans_cand_min_pos
        elif not None in {ans_cand_min_pos,remain_cand_max_neg}:
            ans_cand.append(remain_cand_max_neg)
            NG=ans_cand_min_pos
        elif not None in {ans_cand_min_neg,remain_cand_max_pos}:
            ans_cand.append(remain_cand_max_pos)
            NG=ans_cand_min_neg


        for a in ans_cand:
            if a!=NG:
                ans*=a
                ans%=MOD
            else:
                NG=None
print(ans)
