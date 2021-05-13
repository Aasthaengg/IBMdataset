n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if a[i]<0:
        s+=1
        a[i]*=-1
if s%2==0:
    print(sum(a))
else:
    a.sort()
    print(sum(a)-2*a[0])