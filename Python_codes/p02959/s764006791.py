n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

kills = 0
b_k = 0

for i in range(n):
    b_k = b[i]
    for j in range(2):
        if b_k - a[i+j] >= 0:
            kills += a[i+j]
            b_k -= a[i+j]
            a[i+j] = 0
        else:
            kills += b_k
            a[i+j] -= b_k
            b_k = 0

print(kills)