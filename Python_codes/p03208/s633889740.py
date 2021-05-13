n, k = map(int, input().split())
lis = []
for _ in range(n):
    lis.append(int(input()))
    
lis = sorted(lis)

tmp = 10000000000

for i in range(n-k+1):
    ma = lis[i+k-1]
    mi = lis[i]
    
    tmp = min(tmp, ma-mi)
    
print(tmp)