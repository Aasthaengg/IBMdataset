n,x = map(int,input().split())
m = []
for _ in range(n):
    m.append(int(input()))

m.sort()

print(n + (x - sum(m))//m[0])
