N=int(input())

#Nが完全グラフの辺の数に等しい場合Yes
e=0
v=1
while e<=10**5:
    if e==N: break
    e+=v
    v+=1
else:
    print('No')
    exit()
print('Yes')

#部分集合の数=頂点数
#部分集合内の要素数=ひとつの頂点から出ている辺の数=e*2/v
subsets=[set() for _ in range(v)]
k=1
for i in range(v):
    for j in range(i+1,v):
        subsets[i].add(k)
        subsets[j].add(k)
        k+=1

print(v)
for s in subsets:
    S=[len(s)]+list(s)
    print(' '.join(map(str,S)))