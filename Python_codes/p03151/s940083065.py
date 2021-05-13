N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = sorted([A[i]-B[i] for i in range(N)],reverse=True)
cp = 0
cm = 0
cnt = 0
for i in range(N):
    if C[i]>0:
        cp += C[i]
    elif C[i]<0:
        cnt += 1
        cm += -C[i]
if cm>cp:
    print(-1)
elif cnt==0:
    print(0)
else:
    cur = 0
    tot = C[cur]
    for i in range(N):
        if C[i]<0:
            while tot-abs(C[i])<0:
                tot += C[cur+1]
                cur += 1
            tot += C[i]
    print(cur+1+cnt)  