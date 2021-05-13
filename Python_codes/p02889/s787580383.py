n,m,l = map(int, input().split())
wf=[[float("inf") for i in range(n)] for j in range(n)]
for i in range(m):
    a,b,c = list(map(int,input().split()))
    wf[a-1][b-1] = c
    wf[b-1][a-1] = c
q = int(input())
st=[list(map(int,input().split())) for i in range(q)]

for i in range(n):
    wf[i][i]=0
for k in range(n):
    for i in range(n):
        for j in range(i+1,n):
            wf[i][j] = min(wf[i][j],wf[i][k]+wf[k][j])
            wf[j][i] = wf[i][j]

for i in range(n):
    for j in range(n):
        if wf[i][j] <= l:
            wf[i][j] = 1
        else:
            wf[i][j] = float("inf")

for k in range(n):
    for i in range(n):
        for j in range(i+1,n):
            wf[i][j] = min(wf[i][j],wf[i][k]+wf[k][j])
            wf[j][i] = wf[i][j]

for que in st:
    s,t=que
    if wf[s-1][t-1] == float("inf"):
        print(-1)
    else:
        print(wf[s-1][t-1]-1)