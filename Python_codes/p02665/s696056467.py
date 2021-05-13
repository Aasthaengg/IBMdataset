n = int(input())
a = list(map(int,input().split()))
cir = 1
bsum = 1
hantei=0
asum = [0 for i in range(n+1)]
asum[0] = sum(a)
for i in range(1,n+1):
    asum[i] = asum[i-1]-a[i]
#print(asum)
swi = 0
for i in range(n):
    if swi == 1:
        #print(cir,a[i])
        cir = cir-a[i]
    if swi==0:
        if (cir-a[i])*2 < asum[i]:
            cir = (cir-a[i])*2
        else:
            cir = asum[i]
            swi = 1

    bsum += cir
    if cir<=0:
        hantei=1
        break


#print(cir,a[-1])


if hantei==1 or cir!=a[-1]:
    print(-1)
else:
    print(bsum)
