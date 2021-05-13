a=[0,0,0]
a[0],a[1],a[2]=map(int,input().split())
k=int(input())
a=sorted(a)
a[2]=a[2]*(2**k)
print(sum(a))