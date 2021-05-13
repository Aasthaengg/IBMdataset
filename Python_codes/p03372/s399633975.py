N,C=map(int,input().split())
x=[];v=[]
for i in range(N):
    xi,vi=map(int,input().split())
    x.append(xi);v.append(vi)

# 時計回りにj番目までの寿司を（全部）食べて初期位置まで戻った場合の差し引き摂取カロリー
rc=[v[0]-2*x[0]]
for j in range(1,N):
    rc.append(rc[-1]+v[j]-2*(x[j]-x[j-1]))
# print(f'rc:{rc}') #DB
# 時計回りにj番目までの寿司を（必ずしも最後までではなく）食べて初期位置まで戻った場合の差し引き摂取カロリーの最大値
mrc=[rc[0]]
for j in range(1,N):
    mrc.append(max(mrc[-1],rc[j]))
# print(f'mrc:{mrc}')
# 反時計回りにN-1-i番目までの寿司を（全部）食べて退店した場合の差し引き摂取カロリー
ca=[v[N-1]-(C-x[N-1])]
for i in range(1,N):
    ca.append(ca[-1]+v[N-1-i]-(x[N-i]-x[N-1-i]))
# print(f'ca:{ca}')
# 反時計回りにN-1-i番目までの寿司を（必ずしも最後までではなく）食べて退店した場合の差し引き摂取カロリーの最大値
mca=[ca[0]]
for i in range(1,N):
    mca.append(max(mca[-1],ca[i]))
# print(f'mca:{mca}')


# 反時計回りにN-1-j番目までの寿司を食べて初期位置まで戻った場合の差し引き摂取カロリー
ra=[v[N-1]-2*(C-x[N-1])]
for j in range(1,N):
    ra.append(ra[-1]+v[N-1-j]-2*(x[N-j]-x[N-1-j]))
# print(f'ra:{ra}')
mra=[ra[0]]
for j in range(1,N):
    mra.append(max(mra[-1],ra[j]))
# print(f'mra:{mra}')

# 時計回りにi番目までの寿司を食べて退店した場合の差し引き摂取カロリー
cc=[v[0]-x[0]]
for i in range(1,N):
    cc.append(cc[-1]+v[i]-(x[i]-x[i-1]))
# print(f'cc:{cc}')
mcc=[cc[0]]
for i in range(1,N):
    mcc.append(max(mcc[-1],cc[i]))
# print(f'mcc:{mcc}')

ans=0
if N==1:
    ans=max(ans,v[0]-x[0],v[0]-(C-x[0]))
else:
    # まず時計回りに進み，初期位置まで戻って反時計回りに進む場合
    for i in range(N-1):
        ans=max(ans,mrc[i]+mca[N-2-i])
    # 時計回りに全部食べてから初期位置に戻る(i=N-1)場合は考慮する必要がない。
    # そのような食べ方は，反時計回りに進まず，時計回りに全部食べてそのまま退店する場合よりも常に差し引き摂取カロリーが少ない。

    # 時計回りに進み，そのまま退店する場合
    for i in range(N):
        ans=max(ans,mcc[i])

    # まず反時計回りに進み，初期位置まで戻って時計回りに進む場合
    for i in range(N-1):
        ans=max(ans,mra[i],mra[i]+mcc[N-2-i])
    
    # 反時計回りに進み，そのまま退店する場合
    for i in range(N):
        ans=max(ans,mca[i])

print(ans)