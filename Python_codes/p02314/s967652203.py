n, m = map(int, raw_input().split())
c = map(int, raw_input().split())

t = [float('inf') for i in range(n+1)]
t[0] = 0

for i in range(m):
    if c[i] > n:
        break
    else:
        for j in range(c[i], n+1):
            t[j] = min([t[j], t[j-c[i]]+1])
print t[n]