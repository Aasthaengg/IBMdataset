N,M = map(int, input().split())
an_li = list(map(int, input().split()))
an_li.remove(an_li[0])
for i in range(N-1):
    flag = False
    r = []
    li = list(map(int, input().split()))
    li.remove(li[0])
    for t in an_li:
        if t in li:
            a = 1
        else:
            r.append(t)
            flag = True
    if flag:
        for w in r:
            an_li.remove(w)
print(len(an_li))