mod = 10**9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))
h = [0 for _ in range(2001)]
ans_1 = []
mi = 2001
for ai in reversed(a):
    h[ai] += 1
    mi = min(mi, ai)
    if mi == ai: continue
    ans_1.append(sum(h[:ai]))
h = [0 for _ in range(2001)]
ans_2 = []
mi = 2001
for ai in a:
    h[ai] += 1
    mi = min(mi, ai)
    if mi == ai: continue
    ans_2.append(sum(h[:ai]))
print(int((sum(ans_1) * (k * (k+1) // 2)) +
          (sum(ans_2) * (k * (k-1) // 2))) % mod)