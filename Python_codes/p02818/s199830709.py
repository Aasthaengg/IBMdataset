a,b,k=map(int,input().split())

if a>=k:
    a-=k
elif a+b>=k:
    b-=k-a
    a=0
else:
    a=0
    b=0

print('{} {}'.format(a,b))
