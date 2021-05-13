n= int(input())
a = list(map(int,input().split()))
mc = 0
mi = 999999999
hasz=False
for i in range(n):
    if a[i]==0:hasz=True
    else:
        if a[i]<0:
            mc+=1
            a[i]*=-1
        mi = min(mi,a[i])
if hasz or mc%2==0:print(sum(a))
else:print(sum(a)-mi*2)