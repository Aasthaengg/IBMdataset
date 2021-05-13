dic = {}
N,M = map(int,input().split())

dic1 = {}
for i in range(M):
    a,b = map(int,input().split())
    a,b = min(a,b),max(a,b)
    if b == N:
        dic[a]=0
    if a==1:
        dic1[b]=0
ans = False
for tmp in dic1:
    if tmp in dic:
        ans = True
        break
print("POSSIBLE" if ans else "IMPOSSIBLE")