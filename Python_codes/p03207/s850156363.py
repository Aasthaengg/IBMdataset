n = int(input())
p = [0]*n
for i in range(n):
    p[i] = int(input())
maxp = max(p)
print(sum(p)-maxp//2)