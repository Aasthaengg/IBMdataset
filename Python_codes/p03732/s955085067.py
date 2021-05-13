N,W = map(int,input().split())
w1,v = map(int,input().split())
wv = [[v],[],[],[]]
for i in range(N-1):
    w,v = map(int,input().split())
    wv[w-w1].append(v)
for i in range(4):
    wv[i]=[0] + sorted(wv[i],reverse=True)
# 累積和
for i in range(4):
    for j in range(1,len(wv[i])):
        wv[i][j] += wv[i][j-1]
ans = 0
hoge = [0,0,0,0]
for i in range(len(wv[0])):
    hoge[0] = wv[0][i]
    for j in range(len(wv[1])):
        hoge[1] = wv[1][j]
        for k in range(len(wv[2])):
            hoge[2] = wv[2][k]
            for l in range(len(wv[3])):
                hoge[3] = wv[3][l]
                if w1*(i+j+k+l)+j+2*k+3*l > W:
                    break
                else:
                    ans = max(ans,sum(hoge))
print(ans)