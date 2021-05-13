n, m, k = map(int, input().split())
if k % n == 0 or k % m == 0:
    print('Yes')
    exit()
for i in range(n):
    for j in range(m):
        if m*i + n*j - i*j*2 == k:
            print('Yes')
            exit()
print('No')
