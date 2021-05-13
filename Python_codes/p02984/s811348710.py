n=int(input())
l=list(map(int,input().split()))
su=sum(l)//2
aplussum=sum(l[::2])
a=aplussum-su
ret=[0]*n
ret[0]=a
for i in range(1,n):
    ret[i]=l[i-1]-ret[i-1]
print(*[2*x for x in ret])