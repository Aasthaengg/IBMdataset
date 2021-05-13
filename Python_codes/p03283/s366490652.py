
N,M,Q = map(int,input().split())

#iを始点とする列車。のなかでjを終点とする列車の数をもつ配列
ruiseki = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    L,R = map(int,input().split())
    ruiseki[L][R]+=1

#累積和をとります
for i in range(0,N+1,1):
    for j in range(1,N+1,1):
        ruiseki[i][j] = ruiseki[i][j]+ruiseki[i][j-1]

ans = []

#クエリ処理
for q in range(Q):
    l,r = map(int,input().split())

    #始点がl-rにあるものすべての列車のなかで終点がl-rにあるもの
    tmpans = 0
    for i in range(l,r+1,1):
        tmpans += ruiseki[i][r]
    ans.append(tmpans)

for i in range(Q):
    print(ans[i])
