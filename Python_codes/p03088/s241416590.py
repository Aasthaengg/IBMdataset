N = int(input())
mod = 10 ** 9 + 7

# GAC, ACG, A?GC, AG?C, AGC
last_a = [1, 4, 16]
last_g = [1, 4, 15]
last_c = [1, 4, 14]
last_t = [1, 4, 16]
for i in range(3, N):
    last_a.append(last_a[i - 1] + last_g[i - 1] + last_c[i - 1] + last_t[i - 1])
    last_g.append(last_a[i - 1] + last_g[i - 1] + (last_c[i - 1] - last_a[i - 2] + last_g[i - 3]) + last_t[i - 1])
    last_c.append((last_a[i - 1] - last_g[i - 2]) + (last_g[i - 1] - last_a[i - 2] - (last_a[i - 3] * 2)) + last_c[i - 1] + (last_t[i - 1] - last_a[i - 3]))
    last_t.append(last_a[i - 1] + last_g[i - 1] + last_c[i - 1] + last_t[i - 1])

N -= 1
print((last_a[N] + last_g[N] + last_c[N] + last_t[N]) % mod)