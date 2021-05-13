n,y=map(int,input().split())

en=False
for i in range(n+1):
    for q in range(n-i+1):
        cal=i*10000+q*5000+(n-i-q)*1000
        if cal==y:
            print(i,q,n-i-q)
            en=True
            break
    if en:
        break
if not en:
    print("-1 -1 -1")