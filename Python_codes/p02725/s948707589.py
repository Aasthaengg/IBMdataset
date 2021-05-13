K, N = map(int, input().split(' '))
A_ls = list(map(int, input().split(' ')))
rst = 0
for i in range(N):
    l = A_ls[(i + 1) % len(A_ls)] - A_ls[i]
    if l < 0:
        l = A_ls[(i + 1) % len(A_ls)] + K - A_ls[i]
    rst = max(rst, l)
print(K - rst)