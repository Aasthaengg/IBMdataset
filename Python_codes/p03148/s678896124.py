N,K=map(int,input().split())

l=[] # 寿司リスト。ただし，「おいしさ」を第1要素にする
m=[] # 寿司タプルをそのまま入れる
s=set()

for i in range(N):
    t,d=map(int,input().split())
    l.append((d,t))
l.sort(reverse=True) 

ans=K**2
t=0 # 既に食べたことのある種類の寿司を更に食べた回数

i=0 # l内を走査する際の添字
j=0 # m内を操作する際の添え字

for _ in range(K): # _番目に食べる寿司について
    while i<N and l[i][1] in s:
        m.append(l[i]) # そのままmに追加する
        i+=1 # lの先頭の要素を削除せず，
    if (i<N and (m and j<len(m)) and l[i][0]>=m[j][0]-(2*K-1-2*t)) or (not m or j>=len(m)):
        ans+=l[i][0]
        s.add(l[i][1])
        i+=1
    else:
        ans+=m[j][0]-(2*K-1-2*t)
        j+=1
        t+=1

print(ans)