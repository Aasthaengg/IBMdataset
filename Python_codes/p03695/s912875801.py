n = int(input())

a = [int(x) for x in input().split()]

b = [0] * 9
for i in range(n):
    if a[i] // 400 < 8:
        b[a[i] // 400] += 1
    else:
        b[8] += 1

minsum = 0
maxsum = 0

for i in range(8):
    if b[i] > 0:
        minsum += 1

maxsum = minsum
maxsum += b[8]

if minsum == 0:
    minsum = 1

print("{} {}".format(minsum, maxsum))
