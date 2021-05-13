W,H,N = map(int,input().split())
lst = [list(map(int,input().split())) for i in range(N)]

#print(W,H,N)
#print(lst)
#lst = sorted(lst, key=lambda x: x[2])
#print(lst)
Wst = [1]*W
Hst = [1]*H
for i in range(N):
    if lst[i][2] == 1:
        for j in range(lst[i][0]):
            Wst[j] = 0
    if lst[i][2] == 2:
        #print(lst[i][0],W)
        for j in range(lst[i][0],W):
            Wst[j] = 0
    if lst[i][2] == 3:
        for j in range(lst[i][1]):
            Hst[j] = 0
    if lst[i][2] == 4:
        #print(lst[i][0],W)
        for j in range(lst[i][1],H):
            Hst[j] = 0
    
#print(Wst,Hst)
print(sum(Wst)*sum(Hst))