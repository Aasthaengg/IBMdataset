mod = 2019
# import time

a = input()
n = len(a)
x = [0] * n
# begin = time.time()
for i in range(n):
    x[n - i - 1] = int(a[i])
# print("elapsed 1 = ", time.time() - begin)

# begin = time.time()
ans = 0
cnt = [0] * mod
cnt[0] = 1
s = [0] * (n + 1)
e = 1
# print("elapsed 2 = ", time.time() - begin)

# begin = time.time()
for i in range(n):
    s[i + 1] = ((x[i] * e) % mod + s[i]) % mod
    _ = s[i + 1]
    ans += cnt[_]
    cnt[_] += 1
    e = (e * 10) % mod
# print("elapsed 3 = ", time.time() - begin)

print(ans)

