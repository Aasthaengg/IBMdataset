#editorial参照
#星状グラフに追加するのは連結性や総数の把握が困難
#最大の星状グラフから減らすほうがよい
import sys
n,k = map(int,input().split( ))

cnt = (n-2)*(n-1)//2-k

if cnt<0:
    print(-1)
    sys.exit()
edg_ad = []
for v in range(2,n+1):
    if cnt == 0:
        break
    for u in range(2,v):
        if cnt == 0:
            break
        edg_ad.append((u,v))
        cnt -= 1
ans = []
for v in range(2,n+1):
    ans.append((1,v))
ans2 = set(ans)|set(edg_ad)
ans2 = list(ans2)
ans2.sort()
print(len(ans2))####これ
for e in ans2:
    print(*e)

    
   