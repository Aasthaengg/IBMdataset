import heapq
k,t = map(int,input().split())
a = list(map(int,input().split()))
pre = a.index(max(a))
res = 0
while k>0:
    a[pre] -=1
    k -=1
    if k==0:
        break
    else:
        Conf=[]
        Conf = a[:]
        if t>1:
            Conf[pre] = -1
            preV = max(Conf)
            prei = a.index(preV)
            if preV==0:
                res+=1
            else:
                pre = prei
        else:
            res+=1
print(res)