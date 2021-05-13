n,k,l=map(int,input().split())
pq=[list(map(int,input().split())) for _ in [0]*k]
rs=[list(map(int,input().split())) for _ in [0]*l]

gpq=[[] for _ in [0]*n]
[gpq[b-1].append(a-1) for a,b in pq]
[gpq[a-1].append(b-1) for a,b in pq]

grs=[[] for _ in [0]*n]
[grs[b-1].append(a-1) for a,b in rs]
[grs[a-1].append(b-1) for a,b in rs]

memo_set=set()
list_pq=[]
for i in range(n):
    if i not in memo_set:
        q=[i]
        temp_set={i}
        while q:
            qq=q.pop()
            for g in gpq[qq]:
                if g not in temp_set:
                    q.append(g)
                    temp_set.add(g)
                    memo_set.add(g)
        list_pq.append(temp_set)
        
memo_set=set()
list_rs=[]
for i in range(n):
    if i not in memo_set:
        q=[i]
        temp_set={i}
        while q:
            qq=q.pop()
            for g in grs[qq]:
                if g not in temp_set:
                    q.append(g)
                    temp_set.add(g)
                    memo_set.add(g)
        list_rs.append(temp_set)

dict_rs=dict()

for i,d in enumerate(list_rs):
    for j in d:
        dict_rs[j]=i

dict_pq=dict()

ans=[None]*n
for i,d in enumerate(list_pq):
    for j in d:
        no=dict_rs[j]
        if (i,no) in dict_pq.keys():
            ans[j]=dict_pq[(i,no)]
        else:
            a=len(d&list_rs[no])
            dict_pq[(i,no)]=a
            ans[j]=a

print(*ans)