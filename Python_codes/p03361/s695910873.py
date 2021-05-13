H,W=list(map(int,input().split()))

S=[]
for h in range(H):
    S_temp=list(input())
    S.append(S_temp)

S_=[]
for h in range(H):
    for w in range(W):
        if S[h][w]=='.':
            continue
        try:
            S_left=S[h-1][w]
        except:
            S_left='.'
        try:
            S_right=S[h+1][w]
        except:
            S_right='.'
        try:
            S_up=S[h][w-1]
        except:
            S_up='.'
        try:
            S_down=S[h][w+1]
        except:
            S_down='.'
            
        S__=[S_left,S_right,S_up,S_down]
        S_.append(S__)

ans='Yes'
for s_ in S_:
    if '#' not in s_:
        ans='No'
        break
print(ans)