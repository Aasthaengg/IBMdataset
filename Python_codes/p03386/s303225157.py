a,b,k=map(int,input().split())
for i in range(a,b+1):
    if a+k-1>=i or b-k+1<=i:
        print(i)