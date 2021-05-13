n=int(input())
lists=[]
if n>=2:
    for i in range(n):
        a,b=map(int,input().split())
        lists.append([a,b])
    diflist=[]
    for i in range(n):
        for j in range(n):
            if i!=j:
                add=(lists[i][0]-lists[j][0],lists[i][1]-lists[j][1])
                diflist.append(add)
            else:
                continue
    import collections
    dic=collections.Counter(diflist)
    value=dic.values()
    a=max(value)
    print(n-a)
else:
    print(1)