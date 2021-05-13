h,w=map(int,input().split())
c=[list(map(int, input().split())) for _ in range(10)]
A=[list(map(int, input().split())) for _ in range(h)]
o=[c[i][1] for i in range(10)]#初期状態として各iから直接1にいく場合の魔力を入れる
#print(c)
ans=0
#print(o)
for _ in range(10):#o[i],o[j]は更新されていくので、最低10回は回す（最長移動距離が10のため）
    for i in range(10):
        for j in range(10):
            o[i]=min(o[i],c[i][j]+o[j])#例えば4から1に行く場合、直接行くと9かかるが、4→9→1といくと4で済む。
    #print(o)
    
for s in range(h):
    for t in range(w):
        if A[s][t]!=-1:
            ans+=o[A[s][t]]
print(ans)