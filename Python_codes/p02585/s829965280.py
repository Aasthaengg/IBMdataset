N,K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = -float('inf')
for i in range(N):
    piece = i+1
    temp = 0
    hoge = []
    #hogehoge = []
    key = 0
    for j in range(N):
        if j+1 > K:
            key = 1
            break
        piece = P[piece-1]
        temp += C[piece-1]
        #hogehoge.append(C[piece-1])
        hoge.append(temp)
        if piece == i+1:
            break
    if key == 1:
        ans = max(ans,max(hoge))
    elif hoge[-1]<=0:
        ans = max(ans,max(hoge))
    else:
        d = K//len(hoge)
        r = K%len(hoge)
        if r != 0:
            peak = max(hoge[-1]*(d-1)+max(hoge[r:]),hoge[-1]*d+max(hoge[:r]))
        else:
            peak = hoge[-1]*(d-1)+max(hoge)
        ans = max(ans,peak)
print(ans)
