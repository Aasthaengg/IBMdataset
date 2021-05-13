n,l = map(int,input().split())
m = 0
k = float("inf")
for i in range(n):
    m += l + i
    if k > abs(l + i):
        p = l + i
        k = abs(l + i)
print(m-p)