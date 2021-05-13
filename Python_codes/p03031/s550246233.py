def popcount(x):
    x = (x & 0x5555555555555555) + (x >> 1  & 0x5555555555555555)
    x = (x & 0x3333333333333333) + (x >> 2  & 0x3333333333333333)
    x = (x & 0x0f0f0f0f0f0f0f0f) + (x >> 4  & 0x0f0f0f0f0f0f0f0f)
    x = (x & 0x00ff00ff00ff00ff) + (x >> 8  & 0x00ff00ff00ff00ff)
    x = (x & 0x0000ffff0000ffff) + (x >> 16 & 0x0000ffff0000ffff)
    x = (x & 0x00000000ffffffff) + (x >> 32 & 0x00000000ffffffff)
    return x

n, m = map(int, input().split())

mask = []
for i in range(m):
    vals = list(map(int, input().split()))
    bits = 0
    for s in vals[1:]:
        bits |= 1 << (s-1)
    mask.append(bits)
p = list(map(int, input().split()))

cnt = 0
for i in range(1 << n):
    if all([popcount(i & mask[j]) % 2 ^ p[j] == 0 for j in range(m)]):
        cnt += 1
print(cnt)
    

