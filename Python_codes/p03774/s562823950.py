n,m = map(int,input().split())
nl = []
ml = []
for _ in range(n):
    nl.append(list(map(int,input().split())))
for _ in range(m):
    ml.append(list(map(int,input().split())))

for i in range(n):
    tmp=0
    ans=0
    for j in range(m):
        if ans:
            if tmp > abs(nl[i][0] - ml[j][0]) + abs(nl[i][1] - ml[j][1]):
                tmp = abs(nl[i][0] - ml[j][0]) + abs(nl[i][1] - ml[j][1])
                ans=j+1
        else:
            tmp = abs(nl[i][0] - ml[j][0]) + abs(nl[i][1] - ml[j][1])
            ans=j+1
    print(ans)