n,m = map(int,input().split())

hlist = list(map(int,input().split()))

rank_hlist = sorted(hlist)
rank_dict = dict()
for i in range(n):
    rank_dict[rank_hlist[i]] = i

ab_list = []
for i in range(m):
    a, b = map(int,input().split())
    if rank_dict[hlist[a-1]] < rank_dict[hlist[b-1]]:
        a,b = b,a
    ab_list.append([a,b])

good_n = [1]*n

ab_list.sort(key=lambda x:x[0], reverse=True)

for i in range(m):
    ab = ab_list[i]
    if rank_dict[hlist[ab[0]-1]] > rank_dict[hlist[ab[1]-1]]:
        good_n[ab[1]-1] = 0
    elif rank_dict[hlist[ab[0]-1]] == rank_dict[hlist[ab[1]-1]]:
        good_n[ab[0]-1] = 0
        good_n[ab[1]-1] = 0
    
print(good_n.count(1))
