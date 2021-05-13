a,b,c,=map(int,input().split())
k=int(input())
while k>0:
    if max(a,b,c)==c:
        c=2*c
        k-=1
    elif max(a,b,c)==b:
        b=2*b
        k-=1
    else:
        a=2*a
        k-=1
print(sum([a,b,c]))