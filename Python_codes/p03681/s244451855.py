
n,m=map(int,input().split())
if abs(n-m)>1:
    print(0)
elif abs(n-m)==0:
    cnt=1
    for i in range(n,0,-1):
        cnt*=i
        cnt%=10**9+7
    for i in range(n,0,-1):
        cnt*=i
        cnt%=10**9+7
    cnt*=2
    cnt%=10**9+7
    print(cnt)
else:
    cnt=1
    for i in range(n,0,-1):
        cnt*=i
        cnt%=10**9+7
    for i in range(m,0,-1):
        cnt*=i
        cnt%=10**9+7
    print(cnt)
