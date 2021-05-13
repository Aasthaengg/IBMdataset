N,A,B,C=map(int,input().strip().split())
l=[int(input()) for n in range(N)]

AMP=0
BMP=0
CMP=0
MP=10**5

def dfs(S,N,l,A,B,C):
    A_l=0
    B_l=0
    C_l=0
    A_cnt=0
    B_cnt=0
    C_cnt=0
    if len(S)==N:
        #calcurlate length and merge MP
        for n in range(N):
            if S[n]==0:
                pass
            elif S[n]==1:
                A_l+=l[n]
                A_cnt+=1
            elif S[n]==2:
                B_l+=l[n]
                B_cnt+=1
            else:
                C_l+=l[n]
                C_cnt+=1
        #calculate lengthen and shorten MP
        global MP
        if A_cnt>=1 and B_cnt>=1 and C_cnt>=1:
            MP=min(MP,(A_cnt-1+B_cnt-1+C_cnt-1)*10+abs(A-A_l)+abs(B-B_l)+abs(C-C_l))
        return
    else:
        for n in range(4):
            S.append(n)
            dfs(S,N,l,A,B,C)
            S.pop()

dfs([],N,l,A,B,C)
print(MP)