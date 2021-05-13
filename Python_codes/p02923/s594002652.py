n = int(input())
h = list(map(int,input().split()))
p = 0
m = 0

for i in range(n - 1):
    if h[i] >= h[i + 1]:
        m += 1
    else:
        p = max(p,m)
        m = 0

print(max(p,m))