while True:
    a,b=map(int,input().split())
    if (a==b):
        if (a==0):
            break
    if (a<b):
        print(f"{a} {b}")
    else:
        print(f"{b} {a}")
    
