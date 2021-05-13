def f():
    res = []
    for i in range(n):
        pivot = -1
        for j in range(len(LIST)-1,-1,-1):
            if LIST[j] == j:
                pivot = j
                break
        if pivot == -1:
            print(-1)
            exit()
        res.append(pivot+1)
        LIST.pop(pivot)
    res = res[::-1]
    #print(res)
    for v in res:
        print(v)



n = int(input())
LIST = list(map(lambda x:int(x)-1,input().split()))
f()
