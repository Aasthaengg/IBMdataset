N,M=map(int,input().split())
l=[]
for i in range(M):
    l.extend(map(int,input().split()))
for i in range(N):
    print(l.count(i+1))
