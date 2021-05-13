n,r=(int(i)-1 for i in input().strip().split(" "))
ar=[]
for _ in range(r+1):
    a,b=(int(i)-1 for i in input().strip().split(" "))
    ar.append((min(a,b),max(a,b)))

ar.sort()
count=1
cur=ar[0]
for i in range(1,len(ar)):
    if ar[i][0]<cur[1]:
        t=(ar[i][0],min(ar[i][1],cur[1]))
        cur=t
    else:
        count+=1
        cur=ar[i]
print(count)
