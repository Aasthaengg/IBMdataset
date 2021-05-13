n = int(input())
k = int(input())
x = list(map(int, input().split()))


# Bが回収
# Bが回収した場合の距離
b = []
for i in range(n):
    b.append(abs(k - x[i])*2)


# Aが回収
# Aが回収した場合の距離
a = []
for i in range(n):
    a.append(x[i]*2)

# aとbの少ない値を足していく→最小距離
min_len = 0
for i in range(n):
    min_len += min(a[i], b[i])

print(min_len)
