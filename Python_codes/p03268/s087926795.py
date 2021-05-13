n, k = map(int, input().split())
ans = 0
list_N = [0]*k
for num in range(1, n+1):
    m = num % k
    list_N[m] += 1

for a in range(k):
    b = (k-a)%k
    c = (k-a)%k
    if (b+c) % k == 0:
        ans += list_N[a]*list_N[b]*list_N[c]

print(ans)