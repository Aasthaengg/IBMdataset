# 'A'=0, 'C'=1, 'G'=2, 'T'=3 の4進法で考える
p=10**9+7
N=int(input())

a=[[0 for i in range(101)] for x in range(64)]
# a[x][i]は，最後の3桁がxであるようなi桁の文字列の数
# i=3での初期値
for x in range(64):
    if x in [6,9,33]:
        a[x][3]=0
    else:
        a[x][3]=1

# 漸化式
for i in range(3,N):
    for x in range(64):
        if x in [9,33,6]: # XAGC,XGAC,XACG
            a[x][i+1]=0
        elif x in [25,41,57,37,45]: # AXGC(A-:AGC(既出),CGC,GGC,TGC),AGXC(A-:GAC(既出),GCC,GGC(既出),GTC)
            a[x][i+1]=(a[x//4+16][i]+a[x//4+32][i]+a[x//4+48][i])%p
        else:
            a[x][i+1]=(a[x//4][i]+a[x//4+16][i]+a[x//4+32][i]+a[x//4+48][i])%p

ans=0
for x in range(64):
    ans+=a[x][N]
print(ans%p)