N,M = map(int,input().split())
count = 0
if N <= M//2:
    count += N
    M -= N*2
else:
    count += M//2
    M = 0
count += M//4
print(count)