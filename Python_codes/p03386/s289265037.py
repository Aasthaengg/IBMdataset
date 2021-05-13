a,b,k=map(int,input().split())
if a+k<=b-k:
    for i in range(k):
        print(a+i)
    for i in range(k):
        print(b-k+1+i)
else:
    for i in range(a,b+1):
        print(i)
