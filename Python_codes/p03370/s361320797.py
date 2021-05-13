n,x = map(int,input().split())
m = []
c = 0

for _ in range(n):
    m.append(int(input()))

m.sort()
s = sum(m)

x -= s
c += n

c += x//m[0]

print(c)