N,K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
#print(lst)
#print(lst.sort())
lst.sort(key=lambda l:l[0])
#print(lst)

sm = 0
for x in lst:
    sm += x[1]
    #print(lst[i][1])
    if sm >= K:
        print(x[0])
        break