m = int(input())
n = [int(input())for i in range(m)]

minv = n[0]
maxv = -99999999999

for i in range(1,m):
    maxv = max(maxv, (n[i]-minv))
    minv = min(minv, n[i])

print(maxv)