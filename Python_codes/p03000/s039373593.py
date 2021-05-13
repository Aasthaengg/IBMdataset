n,x = map(int,input().split())
L = list(map(int,input().split()))
d = [0] + [0]*n
c = 1
for i in range(n):
    d[i+1] = d[i] + L[i]
    if d[i+1] <= x:
        c += 1
print(c)