N,M = map(int,input().split())
A = [0]*N
for i in range(M):
    a,b = map(lambda x:int(x)-1,input().split())
    A[a] = abs(1-A[a])
    A[b] = abs(1-A[b])
ans = "YES"
for a in A:
    if a:ans="NO"
print(ans)