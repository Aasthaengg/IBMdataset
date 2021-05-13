n=int(input())
d=list(map(int,input().split()))
d.sort()
ABC=[]
ARC=[]
for i in range(n):
    if i<n//2:
        ABC.append(d[i])
    else:
        ARC.append(d[i])
if max(ABC)==min(ARC):
    print(0)
else:
    num=abs(max(ABC)-min(ARC))
    print(num)

