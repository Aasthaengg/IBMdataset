N = int(input())
a = list(map(int, input().split()))

b = [0]*N

xorsum = 0
for i in range(1,N):
    b[i] = b[i-1] ^ a[i-1] ^ a[i]
    xorsum = xorsum ^ b[i]

b[0] = xorsum ^ a[0]

for i in range(1,N):
    b[i] = b[i-1] ^ a[i-1] ^ a[i]

print(" ".join(map(str, b)))