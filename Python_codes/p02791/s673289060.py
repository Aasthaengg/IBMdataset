N = int(input())
ls = list(map(int,input().split()))
ii = 0
minls = N
for i in range(N):    
    if ls[i] <= minls:
        ii += 1
    minls = min(minls,ls[i])

print(ii)