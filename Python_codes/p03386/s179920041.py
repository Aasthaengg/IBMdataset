a,b,k=map(int,input().split())
for i in range(min(k,b-a+1)):
    print(a+i)
for j in range(k-1,-1,-1):
    if a+k-1 < b-j:
        print(b-j)