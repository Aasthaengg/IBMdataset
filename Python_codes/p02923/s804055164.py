N=int(input())
H=list(map(int,input().strip().split()))

cnt=0
maxcnt=0
for n in range(N-1):
    if H[n]>=H[n+1]:
        cnt+=1
    else:
        maxcnt=max(maxcnt,cnt)
        cnt=0
if cnt!=0:
    maxcnt=max(maxcnt,cnt)
print(maxcnt)