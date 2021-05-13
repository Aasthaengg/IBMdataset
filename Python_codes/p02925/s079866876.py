n = int(input())
# 隣接リスト
graph = {i+1000*j:[] for i in range(n) for j in range(i+1,n)}
# 入次数を管理
st = {i+1000*j:0 for i in range(n) for j in range(i+1,n)}


# 入次数が0の頂点の集まり
szero = []

#ソートされたやつたち
ans = []

for i in range(n):
    ls = list(map(int,input().split()))
    f = -1
    for p in ls:
        v = min(i,p-1) + 1000*(max(i,p-1))
        if f != -1:
            graph[f].append(v)
            st[v] += 1
        f = v

for v in st.keys():
    if st[v] == 0:szero.append(v)
count = 0
next_szero = []
while True:
    count += 1
    for i in szero:
        ans.append(i)
        for v in graph[i]:
            st[v] -= 1
            if st[v] == 0:
                next_szero.append(v)
    if len(next_szero) == 0:break
    szero = next_szero
    next_szero = []

if len(ans) != n*(n-1)//2:
    print(-1)
else:
    print(count)