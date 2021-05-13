n = int(input())
a = list(map(int,input().split()))
den = 0
aseki = 1
for i in range(n):
    for j in range(n):
        if i != j:
            aseki *= a[j]
    den += aseki
    aseki = 1
fra = 1
for i in range(n):
    fra *=a[i]
print(fra/den)