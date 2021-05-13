n=int(input())
a=list(map(int , input().split()))
res_o=[0]*n
res_e=[0]*n
res_o[0]=a[0]
res_e[0]=a[0]

o=0
e=0

if res_o[0]<=0:
    o+=1-res_o[0]
    res_o[0]=1
if res_e[0]>=0:
    e+=res_e[0]+1
    res_e[0]=-1

for i in range(1,n):
    res_o[i]=res_o[i-1]+a[i]
    res_e[i]=res_e[i-1]+a[i]
    if i%2==0 and res_o[i]<=0:
        o+=(1-res_o[i])
        res_o[i]=1
    elif i%2==1 and res_o[i]>=0:
        o+=(res_o[i]+1)
        res_o[i]=-1
    if i%2==0 and res_e[i]>=0:
        e+=(1+res_e[i])
        res_e[i]=-1
    elif i%2==1 and res_e[i]<=0:
        e+=(1-res_e[i])
        res_e[i]=1
print(min(e,o))