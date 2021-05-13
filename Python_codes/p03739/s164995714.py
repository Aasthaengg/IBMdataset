N = int(input())
A = list(map(int,input().split()))
tot = 0
cnt = 0
for i in range(N):
    tot += A[i]
    if i%2==0:
        if tot<=0:
            cnt += abs(tot)+1
            tot = 1
    if i%2==1:
        if tot>=0:
            cnt += tot+1
            tot = -1
cmin = cnt
cnt = 0
tot = 0
for i in range(N):
    tot += A[i]
    if i%2==0:
        if tot>=0:
            cnt += tot+1
            tot = -1
    else:
        if tot<=0:
            cnt += abs(tot)+1
            tot = 1
cmin = min(cmin,cnt)
print(cmin)