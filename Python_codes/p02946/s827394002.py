k,x=map(int,input().split())

for i in range(x-k+1,x+k):
    if -1000000<=i and i<=1000000:
        print(i)
