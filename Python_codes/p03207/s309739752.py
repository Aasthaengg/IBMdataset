n = int(input())
p = sorted([int(input()) for _ in range(n)])
a = 0
for i in range(n-1):
    a += p[i]
a += p[-1]//2
print(a)
