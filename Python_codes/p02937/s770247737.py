import bisect

def resolve():
    S = input()
    T=input()

    indexes = dict()

    for i,v in enumerate(S):
        if v in indexes:
            indexes[v].append(i)
        else:
            indexes[v]=[i]

    point =-1
    roops = 0
    for i in T:
        if not i in indexes:
            print(-1)
            return
        
        nxt = bisect.bisect_right(indexes[i],point)

        if nxt == len(indexes[i]):
            roops += 1
            point = indexes[i][0]
        else:
            point = indexes[i][nxt]


    print(len(S)*roops+point + 1)





resolve()