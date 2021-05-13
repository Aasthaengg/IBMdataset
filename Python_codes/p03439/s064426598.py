n=int(input())
n0=0
print(n0)
s=input()
if s=='Vacant':
    exit()
sl=s    # 席lに座っている人の性別
l,r=0,n # 開区間
m=(l+r)//2 # 中央の座標
print(m)
sm=input()
while sm!='Vacant' and l<r:
    if sm==sl and (m-l)%2==0:
        l=m
        sl=sm
    elif sm!=sl and (m-l)%2==1:
        l=m
        sl=sm
    else:
        r=m
    m=(l+r)//2
    print(m)
    sm=input()
if l>=r:
    print(l,r)
