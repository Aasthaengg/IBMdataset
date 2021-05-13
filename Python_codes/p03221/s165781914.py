N, M = map(int,input().split())
array = []
dic = {}
for i in range(M):
    p, y = map(int,input().split())
    array.append((p,y))
    dic[y]=i
array.sort()
ans = ['']*M
now_p = array[0][0]
idx = 1
for p, y in array:
    if p != now_p:
        idx = 1
    now_p = p
    ans[dic[y]]=str(p).zfill(6)+str(idx).zfill(6)
    idx+=1
for a in ans:
    print(a)