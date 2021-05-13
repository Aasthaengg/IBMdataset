a,b=map(int,input().split())
if a==b:
    print(f"{a}"*a)
elif a>b:
    print(f"{b}"*a)
elif a<b:
    print(f"{a}"*b)
