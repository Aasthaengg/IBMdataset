n, m, k = map(int, input().split())
flag = 0

for i in range(n+1):
    for j in range(m+1):
        if (i*m + j*n) -(2*i*j) == k:
            flag = 1
            break

if flag:
    print('Yes')
else:
    print('No')