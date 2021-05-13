n, x = map(int, input().split())
m = []
for i in range(n):
    m.append(int(input()))
x -= sum(m)
ans = n
m.sort()
print(ans+x//m[0])