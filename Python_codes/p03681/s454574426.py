n,m=map(int,input().split())
MOD = 1000000007

if abs(n-m) > 1:
    print(0)
    exit(0)
else:
    n_cnt,m_cnt=1,1
    for i in range(1,n+1):
        n_cnt*=i
        n_cnt%=MOD
    for i in range(1,m+1):
        m_cnt*=i
        m_cnt%=MOD

    if abs(n-m) == 0:
        ans=n_cnt*m_cnt*2
    else:
        ans=n_cnt*m_cnt
print(ans%MOD)