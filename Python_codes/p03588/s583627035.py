n = int(input())
L = []
for i in range(n):
    a,b = map(int,input().split())
    L.append((a,b))
L.sort()

max_zyun = L[0][0]
min_score = L[-1][1]

cnt = n + max_zyun-1 + min_score

for i in range(n-1):
    cnt +=(min(L[i+1][0] - L[i][0] -1,L[i][1] - L[i+1][1]-1))

print(cnt)