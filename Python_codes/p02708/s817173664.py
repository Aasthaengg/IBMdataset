n, k = map(int,input().split())
mod = 10 ** 9 + 7

cnt = 0
for i in range(k, n + 2):
    temp = i * (2 * n - i + 1) // 2 - i * (i - 1) // 2 + 1
    cnt = (cnt + temp) % mod
    #print(i, cnt, temp)
print(cnt)