N,M = map(int,input().split())
L = []
for _ in range(M):
    a,b = map(int,input().split())
    L.append([a,b])
L = sorted(L,key = lambda x:x[1])
cnt = 0
while len(L):
    now = L.pop(0)
    cnt += 1
    while len(L):
        if L[0][0] + 1 <= now[1]  and now[1]  < L[0][1] + 1:
            L.pop(0)
        else:
            break
print(cnt)



