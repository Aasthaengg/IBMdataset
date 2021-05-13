n,d=map(int,input().split())
for i in range(n+1):
    if (2*d+1)*i>=n:
        print(i)
        break