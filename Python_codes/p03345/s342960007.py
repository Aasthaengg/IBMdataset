a,b,c,k=map(int,input().split())
if a==b==c:
    print(0)
    exit()
elif abs(a-b)>10**18:
    print("Unfair")
elif k%2==1:
    print(b-a)
else:
    print(a-b)