import math
while True:
    N=int(input())
    if N==0:
      exit()
    se=0
    L=list(map(int,input().split()))
    ave=sum(L)/N
    for i in range(N):
        se+=(L[i]-ave)*(L[i]-ave)
    ans=math.sqrt(se/N)
    print(round(ans,8))
