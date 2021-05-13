N = int(input())
lsB = list(map(int,input().split()))

lsA = [0]*N
lsA[0] = lsB[0]
lsA[N-1] = lsB[N-2]
for i in range(1,N-1):
    lsA[i] = min(lsB[i-1],lsB[i])
print(sum(lsA))