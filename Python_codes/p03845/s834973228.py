n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
d=0
for i in range(0,len(a)):
        d=d+a[i]
for i in range(m):
    b,c=[int(i) for i in input().split()]
    z=a[b-1]
    e=(d-(z))+(c)
    print(e)