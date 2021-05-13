a,b,c,d,e,f=map(int,input().split())

water=set()#入れる可能性のある水の量O(A*B)
sugar=set()#入れる可能性のある佐藤の量O(C*D)

for i in range(31):
    for j in range(31):
        if 100*i*a+100*j*b<=f:
            water.add(100*i*a+100*j*b)

for i in range(1501):
    for j in range(1501):
        if c*i+d*j<=f:
            sugar.add(c*i+d*j)
water=sorted(list(water))
#print(water)
#print(sugar)
sugar=sorted(list(sugar))
#print(sugar)
ans=0
sugarans=0
sumans=0
for i in range(1,len(water)):
    for j in range(len(sugar)):
        if water[i]+sugar[j]<=f and sugar[j]<=e*(water[i]/100):
            if ans<(100*sugar[j])/(water[i]+sugar[j]):
                #print(sugar[j],water[j])
                ans=(100*sugar[j])/(water[i]+sugar[j])
                sugarans=sugar[j]
                sumans=water[i]+sugar[j]
               # print(ans)
if  sumans==0:
    print(100*a,sugarans)
else:
    print(sumans,sugarans)