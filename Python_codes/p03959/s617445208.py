mod=10**9+7
n=int(input())
rec,cer=tuple(map(int,input().split())),tuple(map(int,input().split()))
table=[-1]*n#確定した山ならば、その高さ。-1は未確定
table[0]=rec[0]
table[-1]=cer[-1]
if rec[-1]!=cer[0]:print(0);exit()#同じ山々を踏破してるので全体の最大値が違うのは矛盾
for i in range(1,n):
    if rec[i]>rec[i-1]:
        if table[i]!=-1 and table[i]!=rec[i]:print(0);exit()
        table[i]=rec[i]
        if cer[i]<table[i]:print(0);exit()
    if cer[n-i-1]>cer[n-i]:
        if table[n-i-1]!=-1 and table[n-i-1]!=cer[n-i-1]:print(0);exit()
        table[n-i-1]=cer[n-i-1]
        if rec[n-i-1]<table[n-i-1]:print(0);exit()
#各人について、「記録が真に増加したなら、その山の高さは確定する」は真。もう一人の情報と矛盾しないかも見る。
start,f=0,0
now=0
won=0
for i in range(n):
    now=max(now,table[i])
    won=max(won,table[-i-1])
    if now!=rec[i] or won!=cer[-i-1]:print(0);exit()
if now!=won:print(0);exit()
#念のため二人の情報と矛盾しないかシミュレーションしておく
ans=1
for i,v in enumerate(table):
    if v==-1 and f==0:
        start=i
        f=1    #[start,?)に連続して高さ未定義の山が続く
    if v!=-1 and f:
        kosuu=i-start #[start,v)であることがわかったので個数は左
        f=0
        ans=ans*pow(min(v,table[start-1]),kosuu,mod)%mod
        #高さ未定義の山が続く群に対して、そいつらは両隣に高さを抑えられるので、場合の数はこうなる
        #table[0]とtable[n-1]については高さが必ず確定するので、両隣に確定済みの山は必ず存在する

print(ans)
