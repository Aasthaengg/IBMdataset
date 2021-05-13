n,m = map(int,input().split())
if m>1 and n>1:
    print((m-2)*(n-2))
elif n==1 and m>1:
    print(m-2)
elif m==1 and n>1:
    print(n-2)
else:
    print(1)