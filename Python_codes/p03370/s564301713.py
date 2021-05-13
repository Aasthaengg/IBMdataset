
N,X = (map(int, input().split()))
m = [0] * N
for i in range(N):
    m[i] = int(input())

for i in range(N):
    X = X - m[i]

min_value = min(m)
ind = m.index(min_value)
count = N

while X - m[ind] >= 0:
    X = X - m[ind]
    count += 1

print(count)
