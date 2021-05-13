n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

#a.sort()
#b.sort()

if a==b:
    print("Yes")
    exit()

suma=sum(a)
sumb=sum(b)


#sum(a)+2*k=sum(b)+k
#k=(sum(a)-sum(b))

k=sumb-suma
#
#1 1 1 6
#2 2 2 3

cnta=0
cntb=0
for i in range(n):
    if a[i]>b[i]:
        cntb+=a[i]-b[i]
    elif a[i]<b[i]:
        cnta+=(-1)*((a[i]-b[i])//2)
#print(k,cntb,cnta)
if cntb<=k and cnta<=k:
    print("Yes")
else:
    print("No")
