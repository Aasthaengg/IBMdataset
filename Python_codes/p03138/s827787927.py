N, K = map(int, input().split())
A = list(map(int, input().split()))
bit = list(bin(K)[2:])
d = len(bit)
count = [0] * d
for a in A:
    b = bin(a)[2:]
    for j in range(d):
        count[d-j-1] += a >> j & 1
less = False
X = 0
for i in range(d):
    X <<= 1
    if less or bit[i] == '1':
        if 2*count[i] < N:
            X += 1
        else:
            less = True
ans = 0
for a in A:
    ans += X ^ a
print(ans)
