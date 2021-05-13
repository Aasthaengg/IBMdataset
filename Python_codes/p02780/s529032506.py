# coding: utf-8
# 隣接するK個のサイコロの和が大きいものを探す

nk = input().split()
N = int(nk[0])
K = int(nk[1])

Ps = [int(p) for p in input().split()]

# 累積和にしてもいいし、1つずつスライドして求めてもいい気がする

max_sum = sum(Ps[:K])
current_sum = max_sum

# K+1 ~ N-1 までスライドして見ていく
for i in range(K, N):
    current_sum -= Ps[i-K]
    current_sum += Ps[i]

    max_sum = max(max_sum, current_sum)


# 1~pのサイコロの期待値: ((1+p) * p / 2) / p = (1 + p) / 2
ans = 1.0 * (max_sum + K) / 2
print(ans)


