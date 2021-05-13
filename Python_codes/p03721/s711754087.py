N,K=map(int,input().split())
c=sorted([list(map(int,input().split()))for _ in range(N)])
for a, b in c:
    K-=b
    if K<=0:
        print(a)
        exit()
