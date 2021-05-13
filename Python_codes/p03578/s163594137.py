N = int(input())
D = list(map(int,input().split()))
CD = {}
for i in range(N):
    if D[i] not in CD:
        CD[D[i]] = 0
    CD[D[i]] += 1
M = int(input())
T = list(map(int,input().split()))
CT = {}
for i in range(M):
    if T[i] not in CT:
        CT[T[i]] = 0
    CT[T[i]] += 1
flag = 0
for t in CT:
    if t not in CD:
        flag = 1
        break
    if CT[t]>CD[t]:
        flag = 1
        break
if flag==1:
    print("NO")
else:
    print("YES")