n = int(input())
a = list(map(int, input().split()))

s = sum(a) // 2
b_0 = (s - sum(a[1::2])) * 2

b = [0] * n
b[0] = b_0

for i in range(n-1):
    b[i+1] = (a[i] - b[i] // 2) * 2

print(" ".join([str(x) for x in b]))