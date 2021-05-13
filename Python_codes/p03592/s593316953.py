n, m, k = map(int, input().split())

if k == 0:
    print('Yes')
    exit()
if k % n == 0 or k % m == 0:
    print('Yes')
    exit()
for i in range(n+1):
    for j in range(m+1):
        area = i*j + (n-i) * (m-j)
        if k == area:
            print('Yes')
            exit()
print('No')