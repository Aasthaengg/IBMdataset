n, k = map(int, input().split())
k = min(k, n - 1)
p = 10 ** 9 + 7
size = n + 100
f_list = [1] * size
if_list = [1] * size
for i in range(1, size):
    f_list[i] = (f_list[i - 1] * i) % p
    if_list[i] = pow(f_list[i], p-2, p)

def cmb(n, r):
    return f_list[n] * if_list[r] * if_list[n-r] % p

# 初期値は0人の部屋が0個の場合
ans = 1
for i in range(1, k + 1):
    ans += cmb(n, i) * cmb(n - 1, i)
    ans = ans % p
print(ans)