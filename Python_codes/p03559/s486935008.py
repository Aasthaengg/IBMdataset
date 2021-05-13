import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = sorted(a)

for i in range(n):
    b[i] = (b[i], bisect.bisect_right(a, b[i]-1))

b = sorted(b)

bsum = [b[0][1]]
b[0] = b[0][0]
for i in range(1, n):
    bsum.append(bsum[i-1] + b[i][1])
    b[i] = b[i][0]

cnt = 0
for i in range(n):
    ind = bisect.bisect_right(b, c[i]-1)

    if ind > 0:
        cnt += bsum[ind-1]

print(cnt)