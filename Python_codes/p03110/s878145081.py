N = int(input())

toshi = 0
for i in range(N):
    x,u = input().split()
    if u == 'JPY':
        toshi += int(x)
    else:
        toshi += float(x)*380000.0
print(toshi)