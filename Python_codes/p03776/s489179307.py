N, A, B = map(int,input().split())
V = list(map(int,input().split()))
V.sort(reverse = True)
Vs=V[:A]
print(sum(Vs)/A)
###################################
Vs = list(set(Vs))
Vs.sort(reverse = True)
###################################
com = [[0]*51 for i in range(51)]
for i in range(51):
    com[i][0] = 1
    for j in range(1, 51):
        com[i][j] = com[i-1][j-1] + com[i-1][j]
###################################
if len(Vs)!=1:
    N = V.count(Vs[-1])
    k = V[:A].count(Vs[-1])
    ans = com[N][k]
else:
    ans = 0
    N = V.count(Vs[0])
    for k in range(A,B+1):
        ans += com[N][k]
print(ans)