n,a,b= list(map(int, input().split()))
if a>b:
    print("0")
    exit(0)
if n==1:
    if a!=b:
        print("0")
    else:
        print("1")
    exit(0)
n-=2;b-=a;a=0
print(b*n+1)