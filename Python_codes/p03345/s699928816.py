a,b,c,k=map(int,input().split())
if abs(b-a)>10**18:
    print("Unfair")
else:
    if k%2==0:
        print(a-b)
    else:
        print(b-a)