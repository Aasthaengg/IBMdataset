N, M = map(int,input().split())
pyi = [[] for n in range(N)]#県ごとの配列
for i in range(M):
    p, y = map(int,input().split())
    pyi[p-1].append([y,i])
    #最終的にはinput順より誕生年と順番組にして保存
#print(pyi)

ans = []#出力用配列
for i in range(N):
    pyi[i].sort()  #県ごとに誕生した年順に
    for j in range(len(pyi[i])): #県の中での出力準備
        ans.append([(6-len(str(i+1)))*"0" + str(i+1) + (6-len(str(j+1)))*"0" + str(j+1),pyi[i][j][1]])
        
ans.sort(key=lambda x:x[1])
for m in range(M):
    print(ans[m][0])
