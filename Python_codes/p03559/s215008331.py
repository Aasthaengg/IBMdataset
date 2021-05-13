n=int(input())
a=sorted([int(_) for _ in input().split()])
b=[int(_) for _ in input().split()]
c=sorted([int(_) for _ in input().split()])
x=0
for i in range(n):
    oa=-1
    na=n
    while na-oa>1:
        ma=(oa+na)//2
        if a[ma]<b[i]:oa=ma
        else:na=ma
    ob=n
    nb=-1
    while ob-nb>1:
        mb=(ob+nb)//2
        if c[mb]>b[i]:ob=mb
        else:nb=mb
    x+=(oa+1)*(n-ob)
print(x)