N,M = list(map(int,input().split()))
lis = []
for i in range(N):
    lis.append([i+1])
for i in range(M):
    a,b = list(map(int,input().split()))
    lis[a-1].append(b)
    lis[b-1].append(a)
for i in range(N):
    print(len(lis[i])-1)