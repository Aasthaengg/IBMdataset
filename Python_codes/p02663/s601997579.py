a,b,c,d,k=map(int,input().split())

if c*60+d-a*60-b<k:
    print(0)
else:
    print(c*60+d-a*60-b-k)