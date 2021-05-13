K, T = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
if K == T:
    print(0)
    exit()

if T == 1:
    print(K - T)
    exit()

b = a[0]
c = a[1]

for i in range(2, T):
    if b >= c:
        c += a[i]
    else:
        b += a[i]

print(max(abs(b - c) - 1, 0))
