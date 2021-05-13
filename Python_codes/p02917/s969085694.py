n = int(input())

blis = list(map(int, input().split()))

alis = [0]*n

alis[0] = blis[0]

for i in range(1, n-1):
    alis[i] = min(blis[i-1], blis[i])
    
alis[n-1] = blis[n-2]

print(sum(alis))
