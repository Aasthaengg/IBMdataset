n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
s=0
k=n
for i in range(1,3*n,2):
    s+=l[i]
    k-=1
    if(k==0):
        break
print(s)
