n,k=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    al=0
    po=0
    for j in range(n):
        if a[i]>a[j]:
            if j<i:
                al+=1
            else:
                po+=1
                al+=1
    l.append((po,al))
ans=0
for i in l:
    ans += i[0]*k+i[1]*(k-1)*k//2
print(ans%(10**9+7))