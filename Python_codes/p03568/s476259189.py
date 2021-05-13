n=int(input())
a=list(map(int,input().split()))

ans1=1 #all
ans2=1 #odd
for i in range(n):
    j=3 #j:all
    k=0 #k:odd
    if (a[i]-1)%2==1:
        k+=1
    if a[i]%2==1:
        k+=1
    if (a[i]+1)%2==1:
        k+=1
    ans1*=j
    ans2*=k
print(ans1-ans2)
