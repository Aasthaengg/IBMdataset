N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

CB = []
for i in range(M):
    b, c = map(int, input().split())
    CB.append([c, b])
CB.sort(reverse=True)
CBCB = [CB[0]]
for i in range(1, M):
    if CB[i][0]==CB[i-1][0]:
        CBCB[-1][1]+= CB[i][1]
    else:
        CBCB.append(CB[i])

ind = 0
ans=0
for l in CBCB:
    if A[ind]>l[0]: # 打ち切り
        break
    elif A[min(ind+l[1]-1, N-1)]<l[0]: #すべて置き換え
        if ind+l[1]>N-1:
            ans+=l[0]*(N-ind)
            ind = N
            break
        else:
            ans+=l[0]*l[1]
            ind+=l[1]
    else:
        sm = ind-1
        la = min(ind + l[1] -1 , N-1)
        while sm+1<la:
            md = (sm+la)//2
            if A[md]>=l[0]:
                la = md
            else:
                sm = md
        ans += l[0]*(sm-ind+1)
        ind = sm+1
        break
        
for i in range(ind, N):
    ans+=A[i]
print(ans)