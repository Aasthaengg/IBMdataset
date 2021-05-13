from collections import deque

N,M = map(int,input().split())

RD = [deque() for i in range(N)]
end = [False] * N

for i in range(M):

    L,R,D = map(int,input().split())
    RD[L-1].append([R-1,D])
    RD[R-1].append([L-1,-1 * D])
    end[L-1] = True
    end[R-1] = True
    
"""
    lp = wantp(L-1)
    rp = wantp(R-1)

    if lp != rp:

        if rank[lp] 
"""
    


endnum = 0
Q = deque()

cor = ["x"] * N
ans = "Yes"


for endp in range(N):

    if end[endp]:
        Q.append(endp)


        while len(Q) > 0:

            q = Q.pop()
            end[q] = False

            if cor[q] == "x":
                cor[q] = 0

            for r,d in RD[q]:

                if cor[r] == "x":
                    cor[r] = cor[q] + d
                    Q.append(r)

                elif cor[r] != cor[q] + d:
                    print ("No")
                    exit()


print ("Yes")
