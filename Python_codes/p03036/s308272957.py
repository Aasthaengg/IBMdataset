n,m,k = map(int, input().split())
for i in range(10):
    k = n*k-m
    print(k)