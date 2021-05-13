K, N = map(int, input().split(' '))
A_ls = list(map(int, input().split(' ')))
max_l = 0
for i in range(N):
    l = A_ls[(i + 1) % N] - A_ls[i]
    if l < 0:
        l = K - A_ls[i] + A_ls[(i + 1) % N]
    max_l = max(max_l, l)
print(K - max_l)