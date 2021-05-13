n = int(input())
p = list(map(int,input().split()))
c = 0
a = p[0]
for i in range(n):
    c += p[i] <= a
    a = min(p[i],a)
print(c)
