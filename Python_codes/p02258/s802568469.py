n = int(input())

R = []

for i in range(0,n):
    R.insert(i, int(input()))

m = min(R[0:2])
MAX = R[1] - R[0]
for r in range(2, n):
    if(R[r-1] < m):
        m = R[r-1]
    MAX2 = R[r] - m
    if(MAX2 > MAX):
        MAX = MAX2

print(MAX)