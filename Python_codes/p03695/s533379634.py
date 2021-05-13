def cin():  return list(map(int,input().split()))

N = cin()[0]
a = cin()
b = [0 for _ in range(9)]
for i in range(N):
    ind = min(8, a[i] // 400)
    if ind <= 7:  b[ind] = 1
    else:  b[ind] += 1
ma = sum(b)
if b[ind] < N:  mi = sum(b[:-1])
else:  mi = 1
print(mi, ma)