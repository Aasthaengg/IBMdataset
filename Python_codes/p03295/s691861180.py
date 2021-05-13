from sys import stdin
N,M = [int(x) for x in stdin.readline().rstrip().split()]
data = []
for i in range(M):
    a,b = [int(x) for x in stdin.readline().rstrip().split()]
    data.append((b,a))

data.sort()

ans = 1
right = data[0][0]
for b,a in data:
    if a < right:
        continue
    else:
        ans += 1
        right = b
print(ans) 