n, p = map(int, input().split())
a = list(map(int, input().split()))
mod = {0:0, 1:0}
for i in a:
    mod[i % 2] += 1
ans = 0
for i in range(p, mod[1] + 1, 2):
    temp = 1
    for j in range(i):
        temp *= mod[1] - j
        temp //= j + 1
    ans += temp
for i in range(mod[0]):
    ans *= 2
print(ans)