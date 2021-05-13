a,b,c,k=map(int,input().split())
if a>=k:
    print(k)
elif a<k and a+b>=k:
    print(a)
else:
    d=k-a-b
    print(a-d)