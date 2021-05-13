n, x = map(int, input().split())
m = []
for _ in range(n):
    m += [int(input())]

for i in range(n):
    x -= m[i]

mx = min(m)

a = int(x / mx)
 
print(n + a)