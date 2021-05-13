N,M=map(int,input().split())
k=[list(map(int,input().split())) for _ in range(M)] 
*p,=map(int,input().split())
t=0
a=0
for i in range(2 ** N): # 点灯しているスイッチ
    t=0
    for j in range(M): # それぞれの電球
        #print(k[j][0],k[j][1:],p[j])
        o=sum(1 for h in k[j][1:] if i>>(h-1)&1) # onしているスイッチの個数
        #print('{:05b}'.format(i),j+1,o)
        if o%2==p[j]:
            t+=1
    if t==M:
        a+=1
print(a)