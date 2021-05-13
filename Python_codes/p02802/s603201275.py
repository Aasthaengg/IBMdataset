N,M = map(int,input().split())

judge = [False]*N
WAcnt = [0] * N
ACcnt = 0
for i in range(M):
    p,S = (x for x in input().split())
    p = int(p)
    if judge[p-1] == False:
        if S == "AC":
            judge[p-1] = True
            ACcnt += 1
        else:
            WAcnt[p-1] += 1

WAans = 0
for i in range(N):
    if judge[i] == True:
        WAans += WAcnt[i]

print(ACcnt,WAans)