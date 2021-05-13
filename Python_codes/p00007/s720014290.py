n = int(input())
d = 100000

for i in range(n):
    d *= 1.05
    if d % 1000:
        d = d - d%1000 + 1000
print(int(d))
