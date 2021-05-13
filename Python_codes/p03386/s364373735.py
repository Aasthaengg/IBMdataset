a,b,k=map(int,input().split())
for i in range(k):
    if a+i<=b:
        print(a+i)
for j in range(k,0,-1):
    if b-j>=a+k-1:
        print(b-j+1)