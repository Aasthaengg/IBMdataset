n,k=map(int,input().split())
l=list(map(int,input().split()))
m=max(l)
table=[[0,0]for i in range(m.bit_length())]
now=0
su=0
cor=1<<(m.bit_length()-1)
for i in range(m.bit_length()):
    p=[0,0]
    for j in range(n):
        p[l[j]%2]+=1
        l[j]//=2
    table[i][0]=p[0]
    table[i][1]=p[1]
if k.bit_length()>m.bit_length():
    now+=k>>m.bit_length()<<m.bit_length()
    su+=now*n
for i in range(m.bit_length()-1,-1,-1):
    p=table[i]
    if p[1]<=p[0] and now+cor<=k:
        su+=p[0]*cor
        now+=cor
    else:
        su+=cor*p[1]
    cor//=2
print(su)