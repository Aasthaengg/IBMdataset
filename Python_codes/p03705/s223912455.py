n,a,b = map(int,input().split())

if a > b:
    print(0)
elif n == 1:
    print(int(a==b))
else:
    print((b-a)*(n-2)+1)