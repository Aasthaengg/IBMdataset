
def wantp(lis,n):

    q = []
    while lis[n] != n:
        q.append(n)
        n = lis[n]

    for i in q:
        lis[i] = n

    return n


N,K,L = map(int,input().split())
rp = [i for i in range(N)]
rank = [1 for i in range(N)]
pqlis = []

for i in range(K):

    P,Q = map(int,input().split())
    P -= 1
    Q -= 1

    PP = wantp(rp,P)
    QP = wantp(rp,Q)
    pqlis.append([P,Q])

    if PP != QP:

        if rank[PP] < rank[QP]:
            rp[PP] = QP

        elif rank[QP] < rank[PP]:
            rp[QP] = PP

        else:
            rp[QP] = PP
            rank[QP] += 1

#print (rp)

tp = [i for i in range(N)]
rank = [1 for i in range(N)]


for i in range(L):

    P,Q = map(int,input().split())
    P-=1
    Q-=1
    pqlis.append([P,Q])

    PP = wantp(tp,P)
    QP = wantp(tp,Q)

    #print (PP,QP,PP2,PQ2)

    if PP != QP:

        if rank[PP] < rank[QP]:
            tp[PP] = QP

        elif rank[QP] < rank[PP]:
            tp[QP] = PP

        else:
            tp[QP] = PP
            rank[QP] += 1

dic = {}

for i in range(N):

    p1 = wantp(rp,i)
    p2 = wantp(tp,i)
    string = str(p1) + "," + str(p2)

    if string not in dic:
        dic[string] = 1
    else:
        dic[string] += 1

for i in range(N):

    p1 = wantp(rp,i)
    p2 = wantp(tp,i)
    string = str(p1) + "," + str(p2)

    print (dic[string])